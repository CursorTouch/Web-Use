"""CDP Security Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class SecurityMethods:
    """
    Methods for the Security domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Security methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables tracking security state changes.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Security.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables tracking security state changes.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Security.enable", params=params, session_id=session_id)
    async def set_ignore_certificate_errors(self, params: setIgnoreCertificateErrorsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable/disable whether all certificate errors should be ignored.    
        Args:
            params (setIgnoreCertificateErrorsParameters, optional): Parameters for the setIgnoreCertificateErrors method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setIgnoreCertificateErrors call.
        """
        return await self.client.send(method="Security.setIgnoreCertificateErrors", params=params, session_id=session_id)