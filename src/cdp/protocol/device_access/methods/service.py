"""CDP DeviceAccess Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DeviceAccessMethods:
    """
    Methods for the DeviceAccess domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceAccess methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable events in this domain.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="DeviceAccess.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disable events in this domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="DeviceAccess.disable", params=params, session_id=session_id)
    async def select_prompt(self, params: selectPromptParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Select a device in response to a DeviceAccess.deviceRequestPrompted event.    
        Args:
            params (selectPromptParameters, optional): Parameters for the selectPrompt method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the selectPrompt call.
        """
        return await self.client.send(method="DeviceAccess.selectPrompt", params=params, session_id=session_id)
    async def cancel_prompt(self, params: cancelPromptParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.    
        Args:
            params (cancelPromptParameters, optional): Parameters for the cancelPrompt method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the cancelPrompt call.
        """
        return await self.client.send(method="DeviceAccess.cancelPrompt", params=params, session_id=session_id)