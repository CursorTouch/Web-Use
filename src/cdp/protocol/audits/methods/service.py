"""CDP Audits Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AuditsMethods:
    """
    Methods for the Audits domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Audits methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def get_encoded_response(self, params: getEncodedResponseParameters | None = None, session_id: str | None = None) -> getEncodedResponseReturns:
        """
    Returns the response body and size if it were re-encoded with the specified settings. Only applies to images.    
        Args:
            params (getEncodedResponseParameters, optional): Parameters for the getEncodedResponse method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getEncodedResponseReturns: The result of the getEncodedResponse call.
        """
        return await self.client.send(method="Audits.getEncodedResponse", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables issues domain, prevents further issues from being reported to the client.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Audits.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Audits.enable", params=params, session_id=session_id)
    async def check_forms_issues(self, params: checkFormsIssuesParameters | None = None, session_id: str | None = None) -> checkFormsIssuesReturns:
        """
    Runs the form issues check for the target page. Found issues are reported using Audits.issueAdded event.    
        Args:
            params (checkFormsIssuesParameters, optional): Parameters for the checkFormsIssues method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    checkFormsIssuesReturns: The result of the checkFormsIssues call.
        """
        return await self.client.send(method="Audits.checkFormsIssues", params=params, session_id=session_id)