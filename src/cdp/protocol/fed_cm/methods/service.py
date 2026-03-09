"""CDP FedCm Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class FedCmMethods:
    """
    Methods for the FedCm domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the FedCm methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for enable.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="FedCm.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for disable.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="FedCm.disable", params=params, session_id=session_id)
    async def select_account(self, params: selectAccountParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for selectAccount.    
        Args:
            params (selectAccountParameters, optional): Parameters for the selectAccount method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the selectAccount call.
        """
        return await self.client.send(method="FedCm.selectAccount", params=params, session_id=session_id)
    async def click_dialog_button(self, params: clickDialogButtonParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for clickDialogButton.    
        Args:
            params (clickDialogButtonParameters, optional): Parameters for the clickDialogButton method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clickDialogButton call.
        """
        return await self.client.send(method="FedCm.clickDialogButton", params=params, session_id=session_id)
    async def open_url(self, params: openUrlParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for openUrl.    
        Args:
            params (openUrlParameters, optional): Parameters for the openUrl method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the openUrl call.
        """
        return await self.client.send(method="FedCm.openUrl", params=params, session_id=session_id)
    async def dismiss_dialog(self, params: dismissDialogParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for dismissDialog.    
        Args:
            params (dismissDialogParameters, optional): Parameters for the dismissDialog method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the dismissDialog call.
        """
        return await self.client.send(method="FedCm.dismissDialog", params=params, session_id=session_id)
    async def reset_cooldown(self, params: resetCooldownParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently dismissed by the user.    
        Args:
            params (resetCooldownParameters, optional): Parameters for the resetCooldown method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resetCooldown call.
        """
        return await self.client.send(method="FedCm.resetCooldown", params=params, session_id=session_id)