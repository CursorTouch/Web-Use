"""CDP Overlay Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class OverlayEvents:
    """
    Events for the Overlay domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Overlay events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_inspect_node_requested(self, callback: Callable[[inspectNodeRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when the node should be inspected. This happens after call to `setInspectMode` or when user manually inspects an element.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: inspectNodeRequestedEvent, session_id: str | None).
        """
        self.client.on('Overlay.inspectNodeRequested', callback)
    def on_node_highlight_requested(self, callback: Callable[[nodeHighlightRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when the node should be highlighted. This happens after call to `setInspectMode`.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: nodeHighlightRequestedEvent, session_id: str | None).
        """
        self.client.on('Overlay.nodeHighlightRequested', callback)
    def on_screenshot_requested(self, callback: Callable[[screenshotRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when user asks to capture screenshot of some area on the page.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: screenshotRequestedEvent, session_id: str | None).
        """
        self.client.on('Overlay.screenshotRequested', callback)
    def on_inspect_panel_show_requested(self, callback: Callable[[inspectPanelShowRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when user asks to show the Inspect panel.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: inspectPanelShowRequestedEvent, session_id: str | None).
        """
        self.client.on('Overlay.inspectPanelShowRequested', callback)
    def on_inspected_element_window_restored(self, callback: Callable[[inspectedElementWindowRestoredEvent, str | None], None] | None = None) -> None:
        """
    Fired when user asks to restore the Inspected Element floating window.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: inspectedElementWindowRestoredEvent, session_id: str | None).
        """
        self.client.on('Overlay.inspectedElementWindowRestored', callback)
    def on_inspect_mode_canceled(self, callback: Callable[[inspectModeCanceledEvent, str | None], None] | None = None) -> None:
        """
    Fired when user cancels the inspect mode.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: inspectModeCanceledEvent, session_id: str | None).
        """
        self.client.on('Overlay.inspectModeCanceled', callback)