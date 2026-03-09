"""CDP Input Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import InputMethods
from .events.service import InputEvents

if TYPE_CHECKING:
    from ...service import Client

class Input(InputMethods, InputEvents):
    """
    Access the Input domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Input domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        InputMethods.__init__(self, client)
        InputEvents.__init__(self, client)