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

    def test_equality_of_equal_endpoints(self) -> None:
        """
        Purpose:
        Ensure that two endpoints constructed from the same IP address and port are equal according to the `__eq__`
        method.

        Prerequisites:
        N/A

        Pass condition(s):
        - The two endpoints are equal
        """
        # Arrange
        ip_address: str = "192.168.0.19"
        port: int = 1337
        endpoint1 = ipendpoint.IPEndpoint(ip_address, port)
        endpoint2 = ipendpoint.IPEndpoint(ip_address, port)

        # Act/assert
        self.assertEqual(endpoint1, endpoint2)

    def test_inequality_of_endpoints_with_different_ips_but_same_port(self) -> None:
        """
        Purpose:
        Ensure that two endpoints constructed from different IP addresses but the same port are not equal.

        Prerequisites:
        N/A

        Pass condition(s):
        - The two endpoints are not equal
        """
        # Arrange
        port: int = 1337
        endpoint1 = ipendpoint.IPEndpoint("192.168.0.19", port)
        endpoint2 = ipendpoint.IPEndpoint("192.168.1.19", port)

        # Act/assert
        self.assertNotEqual(endpoint1, endpoint2)

    def test_inequality_of_endpoints_with_same_ip_but_different_ports(self) -> None:
        """
        Purpose:
        Ensure that two endpoints constructed from the same IP address but different ports are not equal.

        Prerequisites:
        N/A

        Pass condition(s):
        - The two endpoints are not equal
        """
        # Arrange
        ip_address: str = "192.168.0.19"
        endpoint1 = ipendpoint.IPEndpoint(ip_address, 1337)
        endpoint2 = ipendpoint.IPEndpoint(ip_address, 1234)

        # Act/assert
        self.assertNotEqual(endpoint1, endpoint2)

    def test_inequality_of_endpoints_with_different_ips_and_different_ports(self) -> None:
        """
        Purpose:
        Ensure that two endpoints constructed from the same IP address but different ports are not equal.

        Prerequisites:
        N/A

        Pass condition(s):
        - The two endpoints are not equal
        """
        # Arrange
        endpoint1 = ipendpoint.IPEndpoint("192.168.0.19", 1337)
        endpoint2 = ipendpoint.IPEndpoint("192.168.1.19", 1234)

        # Act/assert
        self.assertNotEqual(endpoint1, endpoint2)


if __name__ == "__main__":
    unittest.main()
