"""
IP endpoint module
"""
from __future__ import annotations
import ipaddress
from typing import Generator, Optional, Tuple, Union


class IPEndpoint(object):
    """
    IP Endpoint class
    """

    def __init__(self: IPEndpoint, ip_address: str, port: int) -> None:
        """
        Initialize an `IPEndpoint` object with an IP address and a port.
        """
        self._ip_address: Optional[Union[ipaddress.IPv4Address, ipaddress.IPv6Address]] = None
        self.ip_address: Union[ipaddress.IPv4Address, ipaddress.IPv6Address] = ip_address
        self._port: Optional[int] = None
        self.port: int = port

    def __repr__(self: IPEndpoint) -> str:
        """
        Generate a representational string for an `IPEndpoint` object.
        """
        return f"{self.__class__.__name__}({self.ip_address}, {self.port})"

    def __str__(self: IPEndpoint) -> str:
        """
        Convert an `IPEndpoint` to a string.
        """
        return f"{self.ip_address}:{self.port}"

    def __iter__(self: IPEndpoint) -> Generator:
        """
        Kind of a hack to allow for representation of an `IPEndpoint` object as a `tuple`.
        """
        yield self.ip_address
        yield self.port

    @property
    def ip_address(self: IPEndpoint) -> str:
        """
        Get the IP Address as a string.
        """
        return format(self._ip_address)

    @ip_address.setter
    def ip_address(self: IPEndpoint, ip_address: Union[str, int, bytes]) -> None:
        """
        Set the IP address.
        """
        self._ip_address = ipaddress.ip_address(ip_address)

    @property
    def port(self: IPEndpoint) -> int:
        """
        Get the port as an `int`.
        """
        return self._port

    @port.setter
    def port(self: IPEndpoint, port: int) -> None:
        """
        Validate and set the port. If invalid, raise `ValueError`.
        """
        if 0 < port <= 65353:
            self._port = port
            return
        raise ValueError(f"Invalid port: {port}")
