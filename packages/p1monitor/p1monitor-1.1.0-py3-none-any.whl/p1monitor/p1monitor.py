"""Asynchronous Python client for the P1 Monitor API."""
from __future__ import annotations

import asyncio
from collections.abc import Mapping
from dataclasses import dataclass
from importlib import metadata
from typing import Any

from aiohttp.client import ClientError, ClientResponseError, ClientSession
from aiohttp.hdrs import METH_GET
from async_timeout import timeout
from yarl import URL

from .exceptions import P1MonitorConnectionError, P1MonitorError
from .models import Phases, Settings, SmartMeter


@dataclass
class P1Monitor:
    """Main class for handling connections with the P1 Monitor API."""

    host: str
    request_timeout: int = 10
    session: ClientSession | None = None

    _close_session: bool = False

    async def request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: Mapping[str, str] | None = None,
    ) -> dict[str, Any]:
        """Handle a request to a P1 Monitor device.

        Args:
            uri: Request URI, without '/api/', for example, 'status'
            method: HTTP Method to use.
            params: Extra options to improve or limit the response.

        Returns:
            A Python dictionary (JSON decoded) with the response from
            the P1 Monitor API.

        Raises:
            P1MonitorConnectionError: An error occurred while communicating
                with the P1 Monitor.
            P1MonitorError: Received an unexpected response from the P1 Monitor API.
        """
        version = metadata.version(__package__)
        url = URL.build(scheme="http", host=self.host, path="/api/").join(URL(uri))

        headers = {
            "User-Agent": f"PythonP1Monitor/{version}",
            "Accept": "application/json, text/plain, */*",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                )
                response.raise_for_status()
        except asyncio.TimeoutError as exception:
            raise P1MonitorConnectionError(
                "Timeout occurred while connecting to P1 Monitor device"
            ) from exception
        except (ClientError, ClientResponseError) as exception:
            raise P1MonitorConnectionError(
                "Error occurred while communicating with P1 Monitor device"
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            text = await response.text()
            raise P1MonitorError(
                "Unexpected response from the P1 Monitor device",
                {"Content-Type": content_type, "response": text},
            )

        return await response.json()

    async def smartmeter(self) -> SmartMeter:
        """Get the latest values from you smart meter.

        Returns:
            A SmartMeter data object from the P1 Monitor API.
        """
        data = await self.request(
            "v1/smartmeter", params={"json": "object", "limit": 1}
        )
        return SmartMeter.from_dict(data)

    async def settings(self) -> Settings:
        """Receive the set price values for energy and gas.

        Returns:
            A Settings data object from the P1 Monitor API.
        """
        data = await self.request("v1/configuration", params={"json": "object"})
        return Settings.from_dict(data)

    async def phases(self) -> Phases:
        """Receive data from all phases on your smart meter.

        Returns:
            A Phases data object from the P1 Monitor API.
        """
        data = await self.request("v1/status", params={"json": "object"})
        return Phases.from_dict(data)

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> P1Monitor:
        """Async enter.

        Returns:
            The P1 Monitor object.
        """
        return self

    async def __aexit__(self, *_exc_info) -> None:
        """Async exit.

        Args:
            _exc_info: Exec type.
        """
        await self.close()
