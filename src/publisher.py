"""
Publisher module
"""
from __future__ import annotations
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from src.configuration import PublisherConfiguration
from src.ipendpoint import IPEndpoint
from src.message import MessageType, Message
from src.messager import MessageProcessor, Messager


class Publisher(Messager):
    """
    Publisher class
    """

    def __init__(self: Publisher, configuration: PublisherConfiguration) -> None:
        """
        Initialize a Publisher object
        """
        super().__init__(configuration)
        self.endpoint = configuration.endpoint
        self.subscriptions: Dict[str, List[Tuple[IPEndpoint, datetime]]] = {}
        self.subscriber_timeout_s: float = configuration.subscriber_timeout_s
        self._message_dispatcher: Dict[str, MessageProcessor] = {
            MessageType.SUBSCRIBE: self._process_subscribe,
            MessageType.SUBMIT: self._process_submit
        }
        print("Initialized Publisher")
        print(f"  Endpoint:    {self.endpoint}")
        print(f"  Buffer size: {self._buffer_size_b}")

    def run(self: Publisher) -> None:
        """
        Run the Publisher
        """
        self._socket.bind(tuple(self.endpoint))
        super().run()

    def _execute(self: Publisher) -> None:
        """
        Main Publisher code
        """
        print("Waiting for a message...")
        message, remote_endpoint = self._receive_message()
        response: Optional[str] = self._process_message(message, remote_endpoint)
        if response:
            self._send_message(response, remote_endpoint)
        self._remove_timed_out_subscribers()

    def _process_subscribe(self: Publisher, subscribe_message: Message, endpoint: IPEndpoint) -> Message:
        """
        Process a subscription request
        """
        for publication in subscribe_message.payload:
            print(f"  Added subscription to {publication}")
            timestamp: datetime = subscribe_message.timestamp
            self.subscriptions[publication] = [*self.subscriptions.get(publication, list()), (endpoint, timestamp)]
        subscribe_message.timestamp = datetime.now()
        return subscribe_message

    def _process_submit(self: Publisher, submit_message: Message, endpoint: IPEndpoint) -> None:
        """
        Process a published message
        """
        if not submit_message.payload:
            print(f"Invalid submit message: {submit_message}")
            return
        publication: str = submit_message.payload[0]
        publish_message = Message(MessageType.PUBLISH, datetime.now(), publication, *submit_message.payload[1:])
        for subscriber_endpoint, _ in self.subscriptions.get(publication, list()):
            self._send_message(publish_message, subscriber_endpoint)

    def _remove_timed_out_subscribers(self) -> None:
        """
        Check for and remove any timed-out subscribers
        """
        now = datetime.now()
        for publication, subscribers in self.subscriptions.items():
            self.subscriptions[publication] = [
                s for s in subscribers if (now - s[1]).total_seconds() < self.subscriber_timeout_s
            ]
