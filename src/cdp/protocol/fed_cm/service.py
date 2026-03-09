"""CDP FedCm Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import FedCmMethods
from .events.service import FedCmEvents

if TYPE_CHECKING:
    from ...service import Client

class FedCm(FedCmMethods, FedCmEvents):
    """
    This domain allows interacting with the FedCM dialog.
    """
    def __init__(self, client: Client):
        """
        Initialize the FedCm domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        FedCmMethods.__init__(self, client)
        FedCmEvents.__init__(self, client)