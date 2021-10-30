"""
Messager module
"""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
import socket
import time
from typing import Callable, Dict, Optional, Tuple

from src.configuration import Configuration
from src.ipendpoint import IPEndpoint
from src.message import Message


MessageProcessor = Callable[[Message, IPEndpoint], Optional[Message]]


class Messager(object):
    """
    Messager class

    Intended to act as a base class for publisher and subscriber classes.
    """

    def __init__(self: Messager, configuration: Configuration) -> None:
        """
        Initialize a Messager object
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.settimeout(configuration.socket_timeout_s)
        self._buffer_size_b: int = configuration.buffer_size_b
        self._messages_sent_count: int = 0
        self._messages_received_count: int = 0
        self._message_dispatcher: Dict[str, MessageProcessor] = {}

    def run(self: Messager) -> None:
        """
        Run the Messager
        """
        print(f"Running {__class__.__name__}...")
        try:
            while True:
                self._execute()
        except Exception as e:
            self._socket.close()
            raise e
        print(f"Terminating  {__class__.__name__}")

    def _execute(self: Messager) -> None:
        """
        Abstract method. Subclasses should implement the main code to be executed in the `run` method here.
        """
        raise NotImplementedError(f"Attempted to call abstract method {__class__.__name__}._execute")

    def _send_message(self: Publisher, message: Message, endpoint: IPEndpoint) -> None:
        """
        Send a message
        """
        print(f"Sending message to {endpoint} [#{self._messages_sent_count:5d}]: {message}")
        self._socket.sendto(bytes(message), tuple(endpoint))
        self._messages_sent_count += 1

    def _receive_message(self: Messager) -> Tuple[Message, IPEndpoint]:
        """
        Receive a message
        """
        while True:
            try:
                binary_message, address = self._socket.recvfrom(self._buffer_size_b)
                break
            except (socket.timeout, ConnectionResetError):
                continue
        message = Message.from_bytes(binary_message)
        remote_endpoint = IPEndpoint(address[0], address[1])
        self._messages_received_count += 1
        print(f"Received message from {remote_endpoint} [#{self._messages_received_count:5d}]: {message}")
        return message, remote_endpoint

    def _process_message(self: Messager, message: Message, endpoint: IPEndpoint) -> Optional[Message]:
        """
        Process a message
        """
        print(f"Processing message from {endpoint}: {message}...")
        start_time: float = time.perf_counter()
        response: Optional[str] = self._message_dispatcher.get(
            message.message_type,
            lambda *args: print(f"Unhandled message type: {message.message_type}")
        )(message, endpoint)
        print(f"Processed message in {time.perf_counter() - start_time:.3f} seconds: {message}")
        return response
