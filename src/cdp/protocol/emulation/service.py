"""CDP Emulation Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import EmulationMethods
from .events.service import EmulationEvents

if TYPE_CHECKING:
    from ...service import Client

class Emulation(EmulationMethods, EmulationEvents):
    """
    This domain emulates different environments for the page.
    """
    def __init__(self, client: Client):
        """
        Initialize the Emulation domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        EmulationMethods.__init__(self, client)
        EmulationEvents.__init__(self, client)