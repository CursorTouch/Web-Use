"""CDP Log Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import LogMethods
from .events.service import LogEvents

if TYPE_CHECKING:
    from ...service import Client

class Log(LogMethods, LogEvents):
    """
    Provides access to log entries.
    """
    def __init__(self, client: Client):
        """
        Initialize the Log domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        LogMethods.__init__(self, client)
        LogEvents.__init__(self, client)