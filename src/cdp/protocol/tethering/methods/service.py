"""CDP Tethering Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class TetheringMethods:
    """
    Methods for the Tethering domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Tethering methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def bind(self, params: bindParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Request browser port binding.    
        Args:
            params (bindParameters, optional): Parameters for the bind method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the bind call.
        """
        return await self.client.send(method="Tethering.bind", params=params, session_id=session_id)
    async def unbind(self, params: unbindParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Request browser port unbinding.    
        Args:
            params (unbindParameters, optional): Parameters for the unbind method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the unbind call.
        """
        return await self.client.send(method="Tethering.unbind", params=params, session_id=session_id)