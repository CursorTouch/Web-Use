"""CDP Fetch Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class FetchEvents:
    """
    Events for the Fetch domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Fetch events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_request_paused(self, callback: Callable[[requestPausedEvent, str | None], None] | None = None) -> None:
        """
    Issued when the domain is enabled and the request URL matches the specified filter. The request is paused until the client responds with one of continueRequest, failRequest or fulfillRequest. The stage of the request can be determined by presence of responseErrorReason and responseStatusCode -- the request is at the response stage if either of these fields is present and in the request stage otherwise. Redirect responses and subsequent requests are reported similarly to regular responses and requests. Redirect responses may be distinguished by the value of `responseStatusCode` (which is one of 301, 302, 303, 307, 308) along with presence of the `location` header. Requests resulting from a redirect will have `redirectedRequestId` field set.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: requestPausedEvent, session_id: str | None).
        """
        self.client.on('Fetch.requestPaused', callback)
    def on_auth_required(self, callback: Callable[[authRequiredEvent, str | None], None] | None = None) -> None:
        """
    Issued when the domain is enabled with handleAuthRequests set to true. The request is paused until client responds with continueWithAuth.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: authRequiredEvent, session_id: str | None).
        """
        self.client.on('Fetch.authRequired', callback)