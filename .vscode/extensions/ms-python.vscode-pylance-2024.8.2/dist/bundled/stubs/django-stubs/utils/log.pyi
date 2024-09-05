import logging
from collections.abc import Callable
from logging import LogRecord
from typing import Any

from django.core.management.color import Style

request_logger: Any
DEFAULT_LOGGING: Any

def configure_logging(
    logging_config: str, logging_settings: dict[str, Any]
) -> None: ...

class AdminEmailHandler(logging.Handler):
    include_html: bool = ...
    email_backend: str | None = ...
    def __init__(
        self, include_html: bool = ..., email_backend: str | None = ...
    ) -> None: ...
    def send_mail(
        self, subject: str, message: str, *args: Any, **kwargs: Any
    ) -> None: ...
    def connection(self) -> Any: ...
    def format_subject(self, subject: str) -> str: ...

class CallbackFilter(logging.Filter):
    callback: Callable[..., Any] = ...
    def __init__(self, callback: Callable[..., Any]) -> None: ...
    def filter(self, record: str | LogRecord) -> bool: ...

class RequireDebugFalse(logging.Filter):
    def filter(self, record: str | LogRecord) -> bool: ...

class RequireDebugTrue(logging.Filter):
    def filter(self, record: str | LogRecord) -> bool: ...

class ServerFormatter(logging.Formatter):
    datefmt: None
    style: Style = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def uses_server_time(self) -> bool: ...

def log_response(
    message: str,
    *args: Any,
    response: Any | None = ...,
    request: Any | None = ...,
    logger: Any = ...,
    level: Any | None = ...,
    exc_info: Any | None = ...
) -> None: ...
