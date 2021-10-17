"""
Unit tests for the `message` module
"""
import unittest

from src.message import MessageType, Message


class TestMessageType(unittest.TestCase):
    """
    Unit tests for the `message.MessageType` class
    """

    def test_convert_subscribe_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.SUBSCRIBE from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a lowercase string works
        - Converting a mixed case string works
        - Converting an uppercase string works
        """
        # Arrange
        subscribe_lowercase_string: str = "subscribe"
        subscribe_mixedcase_string: str = "Subscribe"
        subscribe_uppercase_string: str = "SUBSCRIBE"

        # Act
        subscribe_from_lowercase: MessageType = MessageType.from_string(subscribe_lowercase_string)
        subscribe_from_mixedcase: MessageType = MessageType.from_string(subscribe_mixedcase_string)
        subscribe_from_uppercase: MessageType = MessageType.from_string(subscribe_uppercase_string)

        # Assert
        self.assertEqual(subscribe_from_lowercase, MessageType.SUBSCRIBE)
        self.assertEqual(subscribe_from_mixedcase, MessageType.SUBSCRIBE)
        self.assertEqual(subscribe_from_uppercase, MessageType.SUBSCRIBE)

    def test_convert_submit_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.SUBMIT from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a lowercase string works
        - Converting a mixed case string works
        - Converting an uppercase string works
        """
        # Arrange
        submit_lowercase_string: str = "submit"
        submit_mixedcase_string: str = "Submit"
        submit_uppercase_string: str = "SUBMIT"

        # Act
        submit_from_lowercase: MessageType = MessageType.from_string(submit_lowercase_string)
        submit_from_mixedcase: MessageType = MessageType.from_string(submit_mixedcase_string)
        submit_from_uppercase: MessageType = MessageType.from_string(submit_uppercase_string)

        # Assert
        self.assertEqual(submit_from_lowercase, MessageType.SUBMIT)
        self.assertEqual(submit_from_mixedcase, MessageType.SUBMIT)
        self.assertEqual(submit_from_uppercase, MessageType.SUBMIT)

    def test_convert_publish_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.PUBLISH from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a lowercase string works
        - Converting a mixed case string works
        - Converting an uppercase string works
        """
        # Arrange
        publish_lowercase_string: str = "publish"
        publish_mixedcase_string: str = "Publish"
        publish_uppercase_string: str = "PUBLISH"

        # Act
        publish_from_lowercase: MessageType = MessageType.from_string(publish_lowercase_string)
        publish_from_mixedcase: MessageType = MessageType.from_string(publish_mixedcase_string)
        publish_from_uppercase: MessageType = MessageType.from_string(publish_uppercase_string)

        # Assert
        self.assertEqual(publish_from_lowercase, MessageType.PUBLISH)
        self.assertEqual(publish_from_mixedcase, MessageType.PUBLISH)
        self.assertEqual(publish_from_uppercase, MessageType.PUBLISH)

    def test_convert_subscribe_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.SUBSCRIBE to string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Conversion produces the expected string
        """
        # Arrange/act
        subscribe_string_expected: str = "subscribe"
        subscribe_string_created: MessageType = str(MessageType.SUBSCRIBE)

        # Assert
        self.assertEqual(subscribe_string_expected, subscribe_string_created)

    def test_convert_submit_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.SUBMIT to string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Conversion produces the expected string
        """
        # Arrange/act
        submit_string_expected: str = "submit"
        submit_string_created: MessageType = str(MessageType.SUBMIT)

        # Assert
        self.assertEqual(submit_string_expected, submit_string_created)

    def test_convert_publish_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting to MessageType.PUBLISH to string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Conversion produces the expected string
        """
        # Arrange/act
        publish_string_expected: str = "publish"
        publish_string_created: MessageType = str(MessageType.PUBLISH)

        # Assert
        self.assertEqual(publish_string_expected, publish_string_created)


if __name__ == "__main__":
    unittest.main()
