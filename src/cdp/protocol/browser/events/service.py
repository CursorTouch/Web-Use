"""CDP Browser Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class BrowserEvents:
    """
    Events for the Browser domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Browser events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_download_will_begin(self, callback: Callable[[downloadWillBeginEvent, str | None], None] | None = None) -> None:
        """
    Fired when page is about to start a download.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: downloadWillBeginEvent, session_id: str | None).
        """
        self.client.on('Browser.downloadWillBegin', callback)
    def on_download_progress(self, callback: Callable[[downloadProgressEvent, str | None], None] | None = None) -> None:
        """
    Fired when download makes progress. Last call has |done| == true.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: downloadProgressEvent, session_id: str | None).
        """
        self.client.on('Browser.downloadProgress', callback)