"""
Message module
"""
from __future__ import annotations
from datetime import datetime
from enum import auto, IntEnum
from typing import List


TIMESTAMP_FORMAT: str = "%Y%m%d%H%M%S%f"


class MessageType(IntEnum):
    """
    Message type enum
    """

    SUBSCRIBE = auto()
    SUBMIT = auto()
    PUBLISH = auto()

    @classmethod
    def from_string(cls: MessageType, message_type_string: str) -> MessageType:
        """
        Convert a string to a `MessageType` object.
        """
        return {
            "subscribe": cls.SUBSCRIBE,
            "submit": cls.SUBMIT,
            "publish": cls.PUBLISH
        }[message_type_string.lower()]

    def __str__(self: MessageType) -> str:
        """
        Convert a `MessageType` object to a string.
        """
        return self.name.lower()


class Message(object):
    """
    Message class
    """

    @classmethod
    def from_string(cls: Message, message_string: str) -> Message:
        """
        Create a `Message` object from a message string.
        """
        message_type_string, timestamp_string, *payload = message_string.split(",")
        message_type: MessageType = MessageType.from_string(message_type_string)
        timestamp: datetime = datetime.strptime(timestamp_string, TIMESTAMP_FORMAT)
        return cls(message_type, timestamp, *payload)

    @classmethod
    def from_bytes(cls: Message, message_bytes: bytes) -> Message:
        """
        Create a `Message` object from a binary string.
        """
        message_string: str = message_bytes.decode("utf-8")
        return cls.from_string(message_string)

    def __init__(self: Message, message_type: MessageType, timestamp: datetime, *payload: str) -> None:
        """
        Initialize a `Message` object with a message type, a timestamp, and a payload.
        """
        self.message_type: MessageType = message_type
        self.timestamp: datetime = timestamp
        self.payload: List[str] = list(payload)

    def __str__(self: Message) -> str:
        """
        Format a `Message` object as a string.
        """
        tokens: List[str] = [
            str(self.message_type),
            self.timestamp.strftime(TIMESTAMP_FORMAT),
            *self.payload
        ]
        return ",".join(tokens)

    def __bytes__(self: Message) -> bytes:
        """
        Convert a `Message` object as a binary string`.
        """
        return str(self).encode("utf-8")
