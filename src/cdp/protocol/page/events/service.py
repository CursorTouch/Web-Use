"""CDP Page Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PageEvents:
    """
    Events for the Page domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Page events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_dom_content_event_fired(self, callback: Callable[[domContentEventFiredEvent, str | None], None] | None = None) -> None:
        """
    No description available for domContentEventFired.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: domContentEventFiredEvent, session_id: str | None).
        """
        self.client.on('Page.domContentEventFired', callback)
    def on_file_chooser_opened(self, callback: Callable[[fileChooserOpenedEvent, str | None], None] | None = None) -> None:
        """
    Emitted only when `page.interceptFileChooser` is enabled.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: fileChooserOpenedEvent, session_id: str | None).
        """
        self.client.on('Page.fileChooserOpened', callback)
    def on_frame_attached(self, callback: Callable[[frameAttachedEvent, str | None], None] | None = None) -> None:
        """
    Fired when frame has been attached to its parent.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameAttachedEvent, session_id: str | None).
        """
        self.client.on('Page.frameAttached', callback)
    def on_frame_detached(self, callback: Callable[[frameDetachedEvent, str | None], None] | None = None) -> None:
        """
    Fired when frame has been detached from its parent.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameDetachedEvent, session_id: str | None).
        """
        self.client.on('Page.frameDetached', callback)
    def on_frame_subtree_will_be_detached(self, callback: Callable[[frameSubtreeWillBeDetachedEvent, str | None], None] | None = None) -> None:
        """
    Fired before frame subtree is detached. Emitted before any frame of the subtree is actually detached.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameSubtreeWillBeDetachedEvent, session_id: str | None).
        """
        self.client.on('Page.frameSubtreeWillBeDetached', callback)
    def on_frame_navigated(self, callback: Callable[[frameNavigatedEvent, str | None], None] | None = None) -> None:
        """
    Fired once navigation of the frame has completed. Frame is now associated with the new loader.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameNavigatedEvent, session_id: str | None).
        """
        self.client.on('Page.frameNavigated', callback)
    def on_document_opened(self, callback: Callable[[documentOpenedEvent, str | None], None] | None = None) -> None:
        """
    Fired when opening document to write to.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: documentOpenedEvent, session_id: str | None).
        """
        self.client.on('Page.documentOpened', callback)
    def on_frame_resized(self, callback: Callable[[frameResizedEvent, str | None], None] | None = None) -> None:
        """
    No description available for frameResized.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameResizedEvent, session_id: str | None).
        """
        self.client.on('Page.frameResized', callback)
    def on_frame_started_navigating(self, callback: Callable[[frameStartedNavigatingEvent, str | None], None] | None = None) -> None:
        """
    Fired when a navigation starts. This event is fired for both renderer-initiated and browser-initiated navigations. For renderer-initiated navigations, the event is fired after `frameRequestedNavigation`. Navigation may still be cancelled after the event is issued. Multiple events can be fired for a single navigation, for example, when a same-document navigation becomes a cross-document navigation (such as in the case of a frameset).    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameStartedNavigatingEvent, session_id: str | None).
        """
        self.client.on('Page.frameStartedNavigating', callback)
    def on_frame_requested_navigation(self, callback: Callable[[frameRequestedNavigationEvent, str | None], None] | None = None) -> None:
        """
    Fired when a renderer-initiated navigation is requested. Navigation may still be cancelled after the event is issued.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameRequestedNavigationEvent, session_id: str | None).
        """
        self.client.on('Page.frameRequestedNavigation', callback)
    def on_frame_started_loading(self, callback: Callable[[frameStartedLoadingEvent, str | None], None] | None = None) -> None:
        """
    Fired when frame has started loading.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameStartedLoadingEvent, session_id: str | None).
        """
        self.client.on('Page.frameStartedLoading', callback)
    def on_frame_stopped_loading(self, callback: Callable[[frameStoppedLoadingEvent, str | None], None] | None = None) -> None:
        """
    Fired when frame has stopped loading.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: frameStoppedLoadingEvent, session_id: str | None).
        """
        self.client.on('Page.frameStoppedLoading', callback)
    def on_interstitial_hidden(self, callback: Callable[[interstitialHiddenEvent, str | None], None] | None = None) -> None:
        """
    Fired when interstitial page was hidden    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: interstitialHiddenEvent, session_id: str | None).
        """
        self.client.on('Page.interstitialHidden', callback)
    def on_interstitial_shown(self, callback: Callable[[interstitialShownEvent, str | None], None] | None = None) -> None:
        """
    Fired when interstitial page was shown    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: interstitialShownEvent, session_id: str | None).
        """
        self.client.on('Page.interstitialShown', callback)
    def on_javascript_dialog_closed(self, callback: Callable[[javascriptDialogClosedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: javascriptDialogClosedEvent, session_id: str | None).
        """
        self.client.on('Page.javascriptDialogClosed', callback)
    def on_javascript_dialog_opening(self, callback: Callable[[javascriptDialogOpeningEvent, str | None], None] | None = None) -> None:
        """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: javascriptDialogOpeningEvent, session_id: str | None).
        """
        self.client.on('Page.javascriptDialogOpening', callback)
    def on_lifecycle_event(self, callback: Callable[[lifecycleEventEvent, str | None], None] | None = None) -> None:
        """
    Fired for lifecycle events (navigation, load, paint, etc) in the current target (including local frames).    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: lifecycleEventEvent, session_id: str | None).
        """
        self.client.on('Page.lifecycleEvent', callback)
    def on_back_forward_cache_not_used(self, callback: Callable[[backForwardCacheNotUsedEvent, str | None], None] | None = None) -> None:
        """
    Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do not assume any ordering with the Page.frameNavigated event. This event is fired only for main-frame history navigation where the document changes (non-same-document navigations), when bfcache navigation fails.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: backForwardCacheNotUsedEvent, session_id: str | None).
        """
        self.client.on('Page.backForwardCacheNotUsed', callback)
    def on_load_event_fired(self, callback: Callable[[loadEventFiredEvent, str | None], None] | None = None) -> None:
        """
    No description available for loadEventFired.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: loadEventFiredEvent, session_id: str | None).
        """
        self.client.on('Page.loadEventFired', callback)
    def on_navigated_within_document(self, callback: Callable[[navigatedWithinDocumentEvent, str | None], None] | None = None) -> None:
        """
    Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: navigatedWithinDocumentEvent, session_id: str | None).
        """
        self.client.on('Page.navigatedWithinDocument', callback)
    def on_screencast_frame(self, callback: Callable[[screencastFrameEvent, str | None], None] | None = None) -> None:
        """
    Compressed image data requested by the `startScreencast`.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: screencastFrameEvent, session_id: str | None).
        """
        self.client.on('Page.screencastFrame', callback)
    def on_screencast_visibility_changed(self, callback: Callable[[screencastVisibilityChangedEvent, str | None], None] | None = None) -> None:
        """
    Fired when the page with currently enabled screencast was shown or hidden `.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: screencastVisibilityChangedEvent, session_id: str | None).
        """
        self.client.on('Page.screencastVisibilityChanged', callback)
    def on_window_open(self, callback: Callable[[windowOpenEvent, str | None], None] | None = None) -> None:
        """
    Fired when a new window is going to be opened, via window.open(), link click, form submission, etc.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: windowOpenEvent, session_id: str | None).
        """
        self.client.on('Page.windowOpen', callback)
    def on_compilation_cache_produced(self, callback: Callable[[compilationCacheProducedEvent, str | None], None] | None = None) -> None:
        """
    Issued for every compilation cache generated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: compilationCacheProducedEvent, session_id: str | None).
        """
        self.client.on('Page.compilationCacheProduced', callback)