"""CDP SystemInfo Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class SystemInfoMethods:
    """
    Methods for the SystemInfo domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the SystemInfo methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def get_info(self, params: getInfoParameters | None = None, session_id: str | None = None) -> getInfoReturns:
        """
    Returns information about the system.    
        Args:
            params (getInfoParameters, optional): Parameters for the getInfo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getInfoReturns: The result of the getInfo call.
        """
        return await self.client.send(method="SystemInfo.getInfo", params=params, session_id=session_id)
    async def get_feature_state(self, params: getFeatureStateParameters | None = None, session_id: str | None = None) -> getFeatureStateReturns:
        """
    Returns information about the feature state.    
        Args:
            params (getFeatureStateParameters, optional): Parameters for the getFeatureState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getFeatureStateReturns: The result of the getFeatureState call.
        """
        return await self.client.send(method="SystemInfo.getFeatureState", params=params, session_id=session_id)
    async def get_process_info(self, params: getProcessInfoParameters | None = None, session_id: str | None = None) -> getProcessInfoReturns:
        """
    Returns information about all running processes.    
        Args:
            params (getProcessInfoParameters, optional): Parameters for the getProcessInfo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getProcessInfoReturns: The result of the getProcessInfo call.
        """
        return await self.client.send(method="SystemInfo.getProcessInfo", params=params, session_id=session_id)