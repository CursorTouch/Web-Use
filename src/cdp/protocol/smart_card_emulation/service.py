"""CDP SmartCardEmulation Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import SmartCardEmulationMethods
from .events.service import SmartCardEmulationEvents

if TYPE_CHECKING:
    from ...service import Client

class SmartCardEmulation(SmartCardEmulationMethods, SmartCardEmulationEvents):
    """
    Access the SmartCardEmulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the SmartCardEmulation domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        SmartCardEmulationMethods.__init__(self, client)
        SmartCardEmulationEvents.__init__(self, client)