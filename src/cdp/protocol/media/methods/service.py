"""CDP Media Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class MediaMethods:
    """
    Methods for the Media domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Media methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the Media domain    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Media.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the Media domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Media.disable", params=params, session_id=session_id)