"""CDP Tethering Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import TetheringMethods
from .events.service import TetheringEvents

if TYPE_CHECKING:
    from ...service import Client

class Tethering(TetheringMethods, TetheringEvents):
    """
    The Tethering domain defines methods and events for browser port binding.
    """
    def __init__(self, client: Client):
        """
        Initialize the Tethering domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        TetheringMethods.__init__(self, client)
        TetheringEvents.__init__(self, client)