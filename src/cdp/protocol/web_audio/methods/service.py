"""CDP WebAudio Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class WebAudioMethods:
    """
    Methods for the WebAudio domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the WebAudio methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the WebAudio domain and starts sending context lifetime events.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="WebAudio.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the WebAudio domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="WebAudio.disable", params=params, session_id=session_id)
    async def get_realtime_data(self, params: getRealtimeDataParameters | None = None, session_id: str | None = None) -> getRealtimeDataReturns:
        """
    Fetch the realtime data from the registered contexts.    
        Args:
            params (getRealtimeDataParameters, optional): Parameters for the getRealtimeData method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getRealtimeDataReturns: The result of the getRealtimeData call.
        """
        return await self.client.send(method="WebAudio.getRealtimeData", params=params, session_id=session_id)