from abc import ABCMeta, abstractmethod
from typing import List
from mail.models import Message


class EmailBackendABC(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    async def send_messages(self, email_messages: List[Message]) -> None:
        """send all emails in the List"""
        pass

    @abstractmethod
    async def send_message(self, email_message: Message):
        """send a single email"""
        pass
