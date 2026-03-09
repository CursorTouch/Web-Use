"""CDP DeviceOrientation Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DeviceOrientationEvents:
    """
    Events for the DeviceOrientation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceOrientation events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client