"""CDP CSS Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CSSEvents:
    """
    Events for the CSS domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the CSS events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_fonts_updated(self, callback: Callable[[fontsUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded web font.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: fontsUpdatedEvent, session_id: str | None).
        """
        self.client.on('CSS.fontsUpdated', callback)
    def on_media_query_result_changed(self, callback: Callable[[mediaQueryResultChangedEvent, str | None], None] | None = None) -> None:
        """
    Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: mediaQueryResultChangedEvent, session_id: str | None).
        """
        self.client.on('CSS.mediaQueryResultChanged', callback)
    def on_style_sheet_added(self, callback: Callable[[styleSheetAddedEvent, str | None], None] | None = None) -> None:
        """
    Fired whenever an active document stylesheet is added.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: styleSheetAddedEvent, session_id: str | None).
        """
        self.client.on('CSS.styleSheetAdded', callback)
    def on_style_sheet_changed(self, callback: Callable[[styleSheetChangedEvent, str | None], None] | None = None) -> None:
        """
    Fired whenever a stylesheet is changed as a result of the client operation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: styleSheetChangedEvent, session_id: str | None).
        """
        self.client.on('CSS.styleSheetChanged', callback)
    def on_style_sheet_removed(self, callback: Callable[[styleSheetRemovedEvent, str | None], None] | None = None) -> None:
        """
    Fired whenever an active document stylesheet is removed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: styleSheetRemovedEvent, session_id: str | None).
        """
        self.client.on('CSS.styleSheetRemoved', callback)
    def on_computed_style_updated(self, callback: Callable[[computedStyleUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for computedStyleUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: computedStyleUpdatedEvent, session_id: str | None).
        """
        self.client.on('CSS.computedStyleUpdated', callback)