"""CDP Security Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import SecurityMethods
from .events.service import SecurityEvents

if TYPE_CHECKING:
    from ...service import Client

class Security(SecurityMethods, SecurityEvents):
    """
    Access the Security domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Security domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        SecurityMethods.__init__(self, client)
        SecurityEvents.__init__(self, client)