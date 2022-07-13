import asyncio
import logging
from typing import List, Optional, Union
from mail.models import Message
from mail.models import SendInput
from mail.models import Connection
from mail.backends.base import EmailBackendABC
from mail.config import settings

from aiosmtplib import errors
# from aiosmtplib import SMTP
import aiosmtplib


logger = logging.getLogger(__name__)


class EmailBackend(EmailBackendABC):

    def __init__(
        self,
        hostname: str = "",
        port: str = "",
        username: str = "",
        password: str = "",
        use_tls: bool = False,
        timeout: Optional[int] = None
    ):
        self._connection = Connection(
            hostname=hostname or settings.EMAIL_HOST,
            port=port or settings.EMAIL_PORT,
            username=username or settings.EMAIL_HOST_USER,
            password=password or settings.EMAIL_HOST_PASSWORD,
            use_tls=use_tls or settings.EMAIL_USE_TLS,
            timeout=timeout or settings.EMAIL_TIMEOUT
        )

    async def send_messages(self, email_messages: List[Message]):
        tasks = []
        for mail in email_messages:
            task = asyncio.create_task(self._send(mail))
            tasks.append(task)
        # SMTP.send_message() tasks in parallel (i.e. with asyncio.gather())
        # is not any more efficient than executing in sequence, as the client
        # must wait until one mail is sent before beginning the next.
        # If you have a lot of emails to send, consider creating multiple
        # connections (SMTP instances) and splitting the work between them.
        results = asyncio.gather(*tasks, return_exceptions=True)
        logger.info("Results: %s", results)

    async def send_message(self, email_message: Message):
        await self._send(email_message)

    async def _send(self, email_message: Message):
        _input = SendInput(
            message=email_message._message,
            connection=self._connection
        )
        try:
            await aiosmtplib.send(
                email_message._message, **self._connection.dict()
            )
        except errors.SMTPException as err:
            logger.error(err)
            raise
