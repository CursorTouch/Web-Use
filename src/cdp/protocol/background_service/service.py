"""CDP BackgroundService Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import BackgroundServiceMethods
from .events.service import BackgroundServiceEvents

if TYPE_CHECKING:
    from ...service import Client

class BackgroundService(BackgroundServiceMethods, BackgroundServiceEvents):
    """
    Defines events for background web platform features.
    """
    def __init__(self, client: Client):
        """
        Initialize the BackgroundService domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        BackgroundServiceMethods.__init__(self, client)
        BackgroundServiceEvents.__init__(self, client)