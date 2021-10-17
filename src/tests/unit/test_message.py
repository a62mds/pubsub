"""
Unit tests for the `message` module
"""
from datetime import datetime
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


class TestMessage(unittest.TestCase):
    """
    Unit tests for the `message.Message` class
    """

    def test_subscribe_message_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting a subscribe message from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a subscribe message string produces a `Message` object with the correct type, timestamp, and
          payload
        """
        # Arrange
        subscribe_message_string: str = "subscribe,20211017150434567854,publication"

        # Act
        subscribe_message: Message = Message.from_string(subscribe_message_string)

        # Assert
        self.assertEqual(subscribe_message.message_type, MessageType.SUBSCRIBE)
        self.assertEqual(subscribe_message.timestamp, datetime(2021, 10, 17, 15, 4, 34, 567854))
        self.assertEqual(subscribe_message.payload, ["publication"])

    def test_submit_message_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting a submit message from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a submit message string produces a `Message` object with the correct type, timestamp, and
          payload
        """
        # Arrange
        submit_message_string: str = "submit,20211017151511745976,publication,field1,field2"

        # Act
        submit_message: Message = Message.from_string(submit_message_string)

        # Assert
        self.assertEqual(submit_message.message_type, MessageType.SUBMIT)
        self.assertEqual(submit_message.timestamp, datetime(2021, 10, 17, 15, 15, 11, 745976))
        self.assertEqual(submit_message.payload, ["publication", "field1", "field2"])

    def test_publish_message_from_string(self) -> None:
        """
        Purpose:
        Ensure that converting a publish message from string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a publish message string produces a `Message` object with the correct type, timestamp, and
          payload
        """
        # Arrange
        publish_message_string: str = "publish,20211017151756123456,publication,field1,field2,field3,field4"

        # Act
        publish_message: Message = Message.from_string(publish_message_string)

        # Assert
        self.assertEqual(publish_message.message_type, MessageType.PUBLISH)
        self.assertEqual(publish_message.timestamp, datetime(2021, 10, 17, 15, 17, 56, 123456))
        self.assertEqual(publish_message.payload, ["publication", "field1", "field2", "field3", "field4"])

    def test_subscribe_message_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting a subscribe message to a string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a subscribe message produces the expected string representation
        """
        # Arrange
        subscribe_message: Message = Message(
            MessageType.SUBSCRIBE,
            datetime(2021, 10, 17, 15, 4, 34, 567854),
            "publication1", "publication2"
        )
        subscribe_message_string_expected: str = "subscribe,20211017150434567854,publication1,publication2"

        # Act
        subscribe_message_string_created: str = str(subscribe_message)

        # Assert
        self.assertEqual(subscribe_message_string_created, subscribe_message_string_expected)

    def test_submit_message_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting a submit message to a string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a submit message produces the expected string representation
        """
        # Arrange
        submit_message: Message = Message(
            MessageType.SUBMIT,
            datetime(2021, 10, 17, 15, 15, 11, 745976),
            "publication",
            "field1", "field2", "field3"
        )
        submit_message_string_expected: str = "submit,20211017151511745976,publication,field1,field2,field3"

        # Act
        submit_message_string_created: str = str(submit_message)

        # Assert
        self.assertEqual(submit_message_string_created, submit_message_string_expected)

    def test_publish_message_to_string(self) -> None:
        """
        Purpose:
        Ensure that converting a publish message to a string works as expected.

        Prerequisites:
        N/A

        Pass condition(s):
        - Converting a publish message produces the expected string representation
        """
        # Arrange
        publish_message: Message = Message(
            MessageType.PUBLISH,
            datetime(2021, 10, 17, 15, 17, 56, 123456),
            "publication",
            "field1", "field2", "field3", "field4"
        )
        publish_message_string_expected: str = "publish,20211017151756123456,publication,field1,field2,field3,field4"

        # Act
        publish_message_string_created: str = str(publish_message)

        # Assert
        self.assertEqual(publish_message_string_created, publish_message_string_expected)


if __name__ == "__main__":
    unittest.main()
