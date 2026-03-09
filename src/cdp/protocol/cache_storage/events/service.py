"""CDP CacheStorage Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CacheStorageEvents:
    """
    Events for the CacheStorage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the CacheStorage events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client