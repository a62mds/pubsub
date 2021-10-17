"""
Message module
"""
from __future__ import annotations
from enum import auto, IntEnum


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
