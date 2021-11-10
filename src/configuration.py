"""
Configuration module
"""
from __future__ import annotations
from typing import Dict, List, Optional, Union

import yaml

from src.ipendpoint import IPEndpoint


MIN: str = "min"
MAX: str = "max"

IP_ADDRESS: str = "ip-address"
PORT: str = "port"
BUFFER_SIZE_B: str = "buffer-size-b"
SOCKET_TIMEOUT_S: str = "socket-timeout-s"
SUBSCRIBER_TIMEOUT_S: str = "subscriber-timeout-s"
PUBLISHER_IPV4: str = "publisher-ip-address"
PUBLISHER_PORT: str = "publisher-port"
SUBSCRIPTIONS: str = "subscriptions"
PUBLICATIONS: str = "publications"


class Configuration(object):
    """
    Configuration base class
    """

    DEFAULTS: Dict[str, Union[int, float]] = {
        SOCKET_TIMEOUT_S: 0.1,
        BUFFER_SIZE_B: 1024
    }

    LIMITS: Dict[str, Dict[str, Union[int, float]]] = {
        MIN: {
            SOCKET_TIMEOUT_S: 0,
            BUFFER_SIZE_B: 0
        },
        MAX: {
            SOCKET_TIMEOUT_S: 1.0,
            BUFFER_SIZE_B: 16384
        }
    }

    def __init__(
        self: Configuration,
        socket_timeout_s: float,
        buffer_size_b: int
    ) -> None:
        """
        Initialize a `Configuration` object with a socket timeout (in seconds) and a buffer size.
        """
        self._socket_timeout_s: Optional[float] = None
        self.socket_timeout_s: float = socket_timeout_s
        self._buffer_size_b: Optional[int] = None
        self.buffer_size_b: int = buffer_size_b

    @property
    def socket_timeout_s(self: Configuration) -> float:
        """
        Get the socket timeout in seconds.
        """
        return self._socket_timeout_s

    @socket_timeout_s.setter
    def socket_timeout_s(self: Configuration, socket_timeout_s: float) -> None:
        """
        Set the socket timeout in seconds.
        """
        if self.LIMITS[MIN][SOCKET_TIMEOUT_S] < socket_timeout_s <= self.LIMITS[MAX][SOCKET_TIMEOUT_S]:
            self._socket_timeout_s = socket_timeout_s
            return
        raise ValueError(f"Invalid socket timeout: {socket_timeout_s} s")

    @property
    def buffer_size_b(self: Configuration) -> int:
        """
        Get the buffer size in bytes.
        """
        return self._buffer_size_b

    @buffer_size_b.setter
    def buffer_size_b(self: Configuration, buffer_size_b: int) -> None:
        """
        Set the buffer size in bytes.
        """
        if self.LIMITS[MIN][BUFFER_SIZE_B] < buffer_size_b <= self.LIMITS[MAX][BUFFER_SIZE_B]:
            self._buffer_size_b = buffer_size_b
            return
        raise ValueError(f"Invalid buffer size: {buffer_size_b}")


class PublisherConfiguration(Configuration):
    """
    PublisherConfiguration class
    """

    DEFAULTS: Dict[str, Union[int, float]] = {
        **Configuration.DEFAULTS,
        IP_ADDRESS: "127.0.0.1",
        PORT: 5005,
        SUBSCRIBER_TIMEOUT_S: 5
    }

    LIMITS: Dict[str, Dict[str, Union[int, float]]] = {
        MIN: {
            **Configuration.LIMITS[MIN],
            SUBSCRIBER_TIMEOUT_S: 0
        },
        MAX: {
            **Configuration.LIMITS[MAX],
            SUBSCRIBER_TIMEOUT_S: 10
        }
    }

    @classmethod
    def from_yaml(cls: PublisherConfiguration, config_path: Path) -> PublisherConfiguration:
        """
        Read Publisher configuration settings from a YAML file.
        """
        if not config_path.is_file():
            raise FileNotFoundError(f"Cannot find configuration file {config_path}")

        with config_path.open(mode="r") as config_file:
            config: Dict[str, Union[str, int]] = yaml.safe_load(config_file)

        ip_address: str = config.get(IP_ADDRESS, cls.DEFAULTS[IP_ADDRESS])
        port: int = config.get(PORT, cls.DEFAULTS[PORT])
        socket_timeout_s: float = config.get(SOCKET_TIMEOUT_S, cls.DEFAULTS[SOCKET_TIMEOUT_S])
        buffer_size_b: int = config.get(BUFFER_SIZE_B, cls.DEFAULTS[BUFFER_SIZE_B])
        subscriber_timeout_s: float = config.get(SUBSCRIBER_TIMEOUT_S, cls.DEFAULTS[SUBSCRIBER_TIMEOUT_S])

        return cls(ip_address, port, socket_timeout_s, buffer_size_b, subscriber_timeout_s)

    def __init__(
        self: PublisherConfiguration,
        ip_address: str,
        port: int,
        socket_timeout_s: float,
        buffer_size_b: int,
        subscriber_timeout_s: float
    ) -> None:
        """
        Initialize a `PublisherConfiguration` object with an IPv4, a port, a socket timeout (in seconds), a buffer
        size, and a subscriber timeout (in seconds).
        """
        self.endpoint = IPEndpoint(ip_address, port)
        super().__init__(socket_timeout_s, buffer_size_b)
        self._subscriber_timeout_s: Optional[float] = None
        self.subscriber_timeout_s: float = subscriber_timeout_s

    @property
    def subscriber_timeout_s(self: Configuration) -> float:
        """
        Get the subscriber timeout in seconds.
        """
        return self._subscriber_timeout_s

    @subscriber_timeout_s.setter
    def subscriber_timeout_s(self: Configuration, subscriber_timeout_s: float) -> None:
        """
        Set the subscriber timeout in seconds.
        """
        if self.LIMITS[MIN][SUBSCRIBER_TIMEOUT_S] < subscriber_timeout_s <= self.LIMITS[MAX][SUBSCRIBER_TIMEOUT_S]:
            self._subscriber_timeout_s = subscriber_timeout_s
            return
        raise ValueError(f"Invalid subscriber timeout: {subscriber_timeout_s} s")


class SubscriberConfiguration(Configuration):
    """
    SubscriberConfiguration class
    """

    DEFAULTS: Dict[str, Union[int, float]] = {
        **Configuration.DEFAULTS,
        PUBLISHER_IPV4: "127.0.0.1",
        PUBLISHER_PORT: 5005,
    }

    @classmethod
    def from_yaml(cls: SubscriberConfiguration, config_path: Path) -> SubscriberConfiguration:
        """
        Read Subscriber configuration settings from a YAML file.
        """
        if not config_path.is_file():
            raise FileNotFoundError(f"Cannot find configuration file {config_path}")

        with config_path.open(mode="r") as config_file:
            config: Dict[str, Union[str, int]] = yaml.safe_load(config_file)

        publisher_ipv4: str = config.get(PUBLISHER_IPV4, cls.DEFAULTS[PUBLISHER_IPV4])
        publisher_port: int = config.get(PUBLISHER_PORT, cls.DEFAULTS[PUBLISHER_PORT])
        socket_timeout_s: float = config.get(SOCKET_TIMEOUT_S, cls.DEFAULTS[SOCKET_TIMEOUT_S])
        buffer_size_b: int = config.get(BUFFER_SIZE_B, cls.DEFAULTS[BUFFER_SIZE_B])
        subscriptions: Optional[List[str]] = config.get(SUBSCRIPTIONS, [])
        publications: Optional[List[str]] = config.get(PUBLICATIONS, [])

        return cls(publisher_ipv4, publisher_port, socket_timeout_s, buffer_size_b, subscriptions, publications)

    def __init__(
        self: SubscriberConfiguration,
        publisher_ipv4: str,
        publisher_port: int,
        socket_timeout_s: float,
        buffer_size_b: int,
        subscriptions: Optional[List[str]],
        publications: Optional[List[str]]
    ) -> None:
        """
        Initialize a `SubscriberConfiguration` object with a list of subscriptions, a list of publications, an IPv4 for
        the publisher, a port for the publisher, a socket timeout (in seconds), and a buffer size.

        For now, a subscriber cannot simultaneously publish and subscribe to publications.
        """
        self.publisher_endpoint = IPEndpoint(publisher_ipv4, publisher_port)
        super().__init__(socket_timeout_s, buffer_size_b)
        self.subscriptions: Optional[List[str]] = subscriptions
        self.publications: Optional[List[str]] = publications

        self._validate()

    def _validate(self):
        """
        Validate the subscriber configuration.

        Raises:
            ValueError
                - If both subscriptions and publications are specified
                - If subscriptions (publications) is not a list
                - If any publication in subscriptions (publications) is not a string
        """
        if self.subscriptions and self.publications:
            raise ValueError("Cannot have both subscriptions and publications")
        for x in self.subscriptions, self.publications:
            if x is None:
                continue
            if not isinstance(x, list) or not all(isinstance(y, str) for y in x):
                raise ValueError(f"Subscriptions/publications list is invalid: {x}")
