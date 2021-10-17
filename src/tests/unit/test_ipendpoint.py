"""
Unit tests for the `ipendpoint` module
"""
import unittest

from src import ipendpoint


class TestIPEndpoint(unittest.TestCase):
    """
    Unit tests for the `ipendpoint.IPEndpoint` class
    """

    def test_construct_using_valid_ip_address_and_valid_port(self) -> None:
        """
        Purpose:
        Ensure that construction of an `IPEndpoint` object using a valid IP Address and valid port produces a valid
        IPEndpoint object.

        Prerequisites:
        N/A

        Pass condition(s):
        - There should be no exceptions raised.
        - The `ip_address` property should match the IP address used to construct the object.
        - The `port` property should match the port used to construct the object.
        """
        # Arrange
        ip_address: str = "127.0.0.1"
        port: int = 5005

        # Act
        endpoint = ipendpoint.IPEndpoint(ip_address, port)

        # Assert
        self.assertEqual(endpoint.ip_address, ip_address)
        self.assertEqual(endpoint.port, port)

    def test_construct_using_invalid_ip_address_and_valid_port(self) -> None:
        """
        Purpose:
        Ensure that construction of an `IPEndpoint` object using an invalid IP Address raises an exception.

        Prerequisites:
        N/A

        Pass condition(s):
        - A ValueError is raised.
        """
        # Arrange
        ip_address: str = "127.0.1"
        port: int = 5005

        # Act/assert
        with self.assertRaises(ValueError) as context:
            ipendpoint.IPEndpoint(ip_address, port)

    def test_construct_using_valid_ip_address_and_invalid_port(self) -> None:
        """
        Purpose:
        Ensure that construction of an `IPEndpoint` object using an invalid port raises an exception.

        Prerequisites:
        N/A

        Pass condition(s):
        - A ValueError is raised.
        """
        # Arrange
        ip_address: str = "127.0.0.1"
        port: int = -1

        # Act/assert
        with self.assertRaises(ValueError) as context:
            ipendpoint.IPEndpoint(ip_address, port)


if __name__ == "__main__":
    unittest.main()
