"""
Unit tests for the `configuration` module
"""
from pathlib import Path
import unittest

import yaml

from src.configuration import (
    BUFFER_SIZE_B,
    Configuration,
    PublisherConfiguration,
    SOCKET_TIMEOUT_S,
    SubscriberConfiguration
)


UNIT_TEST_CONFIGURATIONS_PATH = Path(__file__).resolve().parent / "configurations"


class TestConfiguration(unittest.TestCase):
    """
    Unit tests for the `configuration.Configuration` class
    """
    pass



class TestPublisherConfiguration(unittest.TestCase):
    """
    Unit tests for the `configuration.PublisherConfiguration` class
    """

    def test_read_basic_publisher_configuration_from_yaml(self) -> None:
        """
        Purpose:
        Ensure that a basic publisher configuration read from a YAML file produces the expected configuration.

        Prerequisites:
        - `src/tests/unit/configurations/test_publisher.yml`

        Pass condition(s):
        - The YAML file is found, read, and parsed successfully with no exceptions raised
        - Settings in `PublisherConfiguration` object agree with those in the YAML file

        Notes:
        - The `src/tests/unit/configurations/test_publisher.yml` file has the following contents:

        ```
        ---
        ip-address: 192.168.0.19
        port: 1337
        ```
        """
        # Arrange
        ip_address: str = "192.168.0.19"
        port: int = 1337
        socket_timeout_s: float = Configuration.DEFAULTS[SOCKET_TIMEOUT_S]
        buffer_size_b: int = Configuration.DEFAULTS[BUFFER_SIZE_B]

        # Act
        config = PublisherConfiguration.from_yaml(UNIT_TEST_CONFIGURATIONS_PATH / "test_publisher.yml")

        # Assert
        self.assertEqual(config.endpoint.ip_address, ip_address)
        self.assertEqual(config.endpoint.port, port)
        self.assertEqual(config.socket_timeout_s, socket_timeout_s)
        self.assertEqual(config.buffer_size_b, buffer_size_b)

    def test_read_full_publisher_configuration_from_yaml(self) -> None:
        """
        Purpose:
        Ensure that a full publisher configuration read from a YAML file produces the expected configuration.

        Prerequisites:
        - `src/tests/unit/configurations/test_publisher_full.yml`

        Pass condition(s):
        - The YAML file is found, read, and parsed successfully with no exceptions raised
        - Settings in `PublisherConfiguration` object agree with those in the YAML file

        Notes:
        - The `src/tests/unit/configurations/test_publisher_full.yml` file has the following contents:

        ```
        ---
        ip-address: 192.168.0.19
        port: 1337
        socket-timeout-s: 0.5
        buffer-size-b: 2048
        ```
        """
        # Arrange
        ip_address: str = "192.168.0.19"
        port: int = 1337
        socket_timeout_s: float = 0.5
        buffer_size_b: int = 2048

        # Act
        config = PublisherConfiguration.from_yaml(UNIT_TEST_CONFIGURATIONS_PATH / "test_publisher_full.yml")

        # Assert
        self.assertEqual(config.endpoint.ip_address, ip_address)
        self.assertEqual(config.endpoint.port, port)
        self.assertEqual(config.socket_timeout_s, socket_timeout_s)
        self.assertEqual(config.buffer_size_b, buffer_size_b)


class TestSubscriberConfiguration(unittest.TestCase):
    """
    Unit tests for the `configuration.SubscriberConfiguration` class
    """

    def test_read_basic_subscriber_configuration_with_subscriptions_from_yaml(self) -> None:
        """
        Purpose:
        Ensure that a basic subscriber configuration with subscriptions read from a YAML file produces the expected
        configuration.

        Prerequisites:
        - `src/tests/unit/configurations/test_subscriber_receiver.yml`

        Pass condition(s):
        - The YAML file is found, read, and parsed successfully with no exceptions raised
        - Settings in `SubscriberConfiguration` object agree with those in the YAML file

        Notes:
        - The `src/tests/unit/configurations/test_subscriber_receiver.yml` file has the following contents:

        ```
        ---
        publisher-ip-address: 192.168.0.19
        publisher-port: 1337
        subscriptions:
        - publication
        ```
        """
        # Arrange
        publisher_ip_address: str = "192.168.0.19"
        publisher_port: int = 1337
        subscriptions = ["publication"]
        socket_timeout_s: float = Configuration.DEFAULTS[SOCKET_TIMEOUT_S]
        buffer_size_b: int = Configuration.DEFAULTS[BUFFER_SIZE_B]

        # Act
        config = SubscriberConfiguration.from_yaml(UNIT_TEST_CONFIGURATIONS_PATH / "test_subscriber_receiver.yml")

        # Assert
        self.assertEqual(config.publisher_endpoint.ip_address, publisher_ip_address)
        self.assertEqual(config.publisher_endpoint.port, publisher_port)
        self.assertEqual(config.subscriptions, subscriptions)
        self.assertEqual(config.publications, [])
        self.assertEqual(config.socket_timeout_s, socket_timeout_s)
        self.assertEqual(config.buffer_size_b, buffer_size_b)

    def test_read_basic_subscriber_configuration_with_publications_from_yaml(self) -> None:
        """
        Purpose:
        Ensure that a basic subscriber configuration with publications read from a YAML file produces the expected
        configuration.

        Prerequisites:
        - `src/tests/unit/configurations/test_subscriber_transmitter.yml`

        Pass condition(s):
        - The YAML file is found, read, and parsed successfully with no exceptions raised
        - Settings in `SubscriberConfiguration` object agree with those in the YAML file

        Notes:
        - The `src/tests/unit/configurations/test_subscriber_transmitter.yml` file has the following contents:

        ```
        ---
        publisher-ip-address: 192.168.0.19
        publisher-port: 1337
        publications:
        - publication
        ```
        """
        # Arrange
        publisher_ip_address: str = "192.168.0.19"
        publisher_port: int = 1337
        publications = ["publication"]
        socket_timeout_s: float = Configuration.DEFAULTS[SOCKET_TIMEOUT_S]
        buffer_size_b: int = Configuration.DEFAULTS[BUFFER_SIZE_B]

        # Act
        config = SubscriberConfiguration.from_yaml(UNIT_TEST_CONFIGURATIONS_PATH / "test_subscriber_transmitter.yml")

        # Assert
        self.assertEqual(config.publisher_endpoint.ip_address, publisher_ip_address)
        self.assertEqual(config.publisher_endpoint.port, publisher_port)
        self.assertEqual(config.subscriptions, [])
        self.assertEqual(config.publications, publications)
        self.assertEqual(config.socket_timeout_s, socket_timeout_s)
        self.assertEqual(config.buffer_size_b, buffer_size_b)

    def test_read_basic_subscriber_configuration_with_publications_and_subscriptions_from_yaml(self) -> None:
        """
        Purpose:
        Ensure that attempting to generate a subscriber configuration with both publications and subscriptions read
        from a YAML file raises an exception.

        Prerequisites:
        - `src/tests/unit/configurations/test_subscriber_transceiver.yml`

        Pass condition(s):
        - The YAML file is found, read, and parsed successfully with no exceptions raised
        - Attempting to create a `SubscriberConfiguration` object from the parsed settings raises a `ValueError`

        Notes:
        - The `src/tests/unit/configurations/test_subscriber_transceiver.yml` file has the following contents:

        ```
        ---
        publisher-ip-address: 192.168.0.19
        publisher-port: 1337
        subscriptions:
        - publication-1
        publications:
        - publication-2
        ```
        """
        with self.assertRaises(ValueError):
            SubscriberConfiguration.from_yaml(UNIT_TEST_CONFIGURATIONS_PATH / "test_subscriber_transceiver.yml")


if __name__ == "__main__":
    unittest.main()
