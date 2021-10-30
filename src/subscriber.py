"""
Subscriber module
"""
from __future__ import annotations
import asyncio
from datetime import datetime
from random import randint, random
import socket
import time
from typing import Callable, List, Optional

from src.configuration import SubscriberConfiguration
from src.ipendpoint import IPEndpoint
from src.message import MessageType, Message
from src.messager import MessageProcessor, Messager


class Subscriber(Messager):
    """
    Subscriber class
    """

    def __init__(self: Subscriber, configuration: SubscriberConfiguration) -> None:
        """
        Initialize a Subscriber object
        """
        super().__init__(configuration)
        self._publisher_endpoint = configuration.publisher_endpoint
        self._subscriptions: List[str] = configuration.subscriptions
        self._publications: List[str] = configuration.publications
        self._is_subscribed: bool = False
        self._responses_received_count: int = 0
        self._publications_received_count: int = 0
        self._requests_sent_count: int = 0
        self._submissions_sent_count: int = 0
        self._message_dispatcher: Dict[str, MessageProcessor] = {
            MessageType.SUBSCRIBE: self._process_subscribe,
            MessageType.PUBLISH: self._process_publish
        }
        print("Initialized a Subscriber object")
        print(f"  Publisher endpoint: {self._publisher_endpoint}")
        print(f"  Subscriptions:      {self._subscriptions}")
        print(f"  Publications:       {self._publications}")

    def subscribe(self: Subscriber) -> bool:
        """
        Subscribe to publications from the Publisher
        """
        subscribe_message = Message(MessageType.SUBSCRIBE, datetime.now(), *self._subscriptions)
        self._send_message(subscribe_message, self._publisher_endpoint)
        self._requests_sent_count += 1
        message, remote_endpoint = self._receive_message()
        self._process_message(message, remote_endpoint)
        return self._is_subscribed

    def submit(self: Subscriber, publication: str, *data: str) -> None:
        """
        Submit data to the Publisher
        """
        submit_message = Message(MessageType.SUBMIT, datetime.now(), publication, *data)
        self._send_message(submit_message, self._publisher_endpoint)
        self._submissions_sent_count += 1

    def _execute(self: Subscriber) -> None:
        """
        Main client code
        """
        if not self._is_subscribed:
            while True:
                try:
                    if self.subscribe():
                        break
                except ConnectionResetError:
                    continue
        if self._subscriptions:
            print("Waiting for a message...")
            message, remote_endpoint = self._receive_message()
            self._process_message(message, remote_endpoint)
        elif self._publications:
            for publication in self._publications:
                self.submit(publication, f"{random():.6f}", f"{random():.6f}", f"{random():.6f}")
                time.sleep(randint(0, 10))
        else:
            print("Nothing to do")

    def _process_subscribe(self: Subscriber, subscribe_message: Message, endpoint: IPEndpoint) -> None:
        """
        Process a subscription response
        """
        self._is_subscribed = True
        self._responses_received_count += 1

    def _process_publish(self: Subscriber, publish_message: Message, endpoint: IPEndpoint) -> None:
        """
        Process a publish message
        """
        self._publications_received_count += 1
