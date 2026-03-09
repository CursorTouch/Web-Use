"""CDP Fetch Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class FetchMethods:
    """
    Methods for the Fetch domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Fetch methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the fetch domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Fetch.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables issuing of requestPaused events. A request will be paused until client calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Fetch.enable", params=params, session_id=session_id)
    async def fail_request(self, params: failRequestParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Causes the request to fail with specified reason.    
        Args:
            params (failRequestParameters, optional): Parameters for the failRequest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the failRequest call.
        """
        return await self.client.send(method="Fetch.failRequest", params=params, session_id=session_id)
    async def fulfill_request(self, params: fulfillRequestParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Provides response to the request.    
        Args:
            params (fulfillRequestParameters, optional): Parameters for the fulfillRequest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the fulfillRequest call.
        """
        return await self.client.send(method="Fetch.fulfillRequest", params=params, session_id=session_id)
    async def continue_request(self, params: continueRequestParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Continues the request, optionally modifying some of its parameters.    
        Args:
            params (continueRequestParameters, optional): Parameters for the continueRequest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the continueRequest call.
        """
        return await self.client.send(method="Fetch.continueRequest", params=params, session_id=session_id)
    async def continue_with_auth(self, params: continueWithAuthParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Continues a request supplying authChallengeResponse following authRequired event.    
        Args:
            params (continueWithAuthParameters, optional): Parameters for the continueWithAuth method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the continueWithAuth call.
        """
        return await self.client.send(method="Fetch.continueWithAuth", params=params, session_id=session_id)
    async def continue_response(self, params: continueResponseParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Continues loading of the paused response, optionally modifying the response headers. If either responseCode or headers are modified, all of them must be present.    
        Args:
            params (continueResponseParameters, optional): Parameters for the continueResponse method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the continueResponse call.
        """
        return await self.client.send(method="Fetch.continueResponse", params=params, session_id=session_id)
    async def get_response_body(self, params: getResponseBodyParameters | None = None, session_id: str | None = None) -> getResponseBodyReturns:
        """
    Causes the body of the response to be received from the server and returned as a single string. May only be issued for a request that is paused in the Response stage and is mutually exclusive with takeResponseBodyForInterceptionAsStream. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior. Note that the response body is not available for redirects. Requests paused in the _redirect received_ state may be differentiated by `responseCode` and presence of `location` response header, see comments to `requestPaused` for details.    
        Args:
            params (getResponseBodyParameters, optional): Parameters for the getResponseBody method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getResponseBodyReturns: The result of the getResponseBody call.
        """
        return await self.client.send(method="Fetch.getResponseBody", params=params, session_id=session_id)
    async def take_response_body_as_stream(self, params: takeResponseBodyAsStreamParameters | None = None, session_id: str | None = None) -> takeResponseBodyAsStreamReturns:
        """
    Returns a handle to the stream representing the response body. The request must be paused in the HeadersReceived stage. Note that after this command the request can't be continued as is -- client either needs to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified. This method is mutually exclusive with getResponseBody. Calling other methods that affect the request or disabling fetch domain before body is received results in an undefined behavior.    
        Args:
            params (takeResponseBodyAsStreamParameters, optional): Parameters for the takeResponseBodyAsStream method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    takeResponseBodyAsStreamReturns: The result of the takeResponseBodyAsStream call.
        """
        return await self.client.send(method="Fetch.takeResponseBodyAsStream", params=params, session_id=session_id)