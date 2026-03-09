"""CDP Page Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.network.types import MonotonicTime
    from cdp.protocol.page.types import BackForwardCacheNotRestoredExplanation
    from cdp.protocol.page.types import BackForwardCacheNotRestoredExplanationTree
    from cdp.protocol.page.types import ClientNavigationDisposition
    from cdp.protocol.page.types import ClientNavigationReason
    from cdp.protocol.page.types import DialogType
    from cdp.protocol.page.types import Frame
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.page.types import NavigationType
    from cdp.protocol.page.types import ScreencastFrameMetadata
    from cdp.protocol.runtime.types import StackTrace

class domContentEventFiredEvent(TypedDict, total=True):
    timestamp: MonotonicTime
class fileChooserOpenedEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame containing input node."""
    mode: Literal["selectSingle", "selectMultiple"]
    """Input mode."""
    backendNodeId: NotRequired[BackendNodeId]
    """Input node id. Only present for file choosers opened via an <input type="file"> element."""
class frameAttachedEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that has been attached."""
    parentFrameId: FrameId
    """Parent frame identifier."""
    stack: NotRequired[StackTrace]
    """JavaScript stack trace of when frame was attached, only set if frame initiated from script."""
class frameDetachedEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that has been detached."""
    reason: Literal["remove", "swap"]
class frameSubtreeWillBeDetachedEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that is the root of the subtree that will be detached."""
class frameNavigatedEvent(TypedDict, total=True):
    frame: Frame
    """Frame object."""
    type: NavigationType
class documentOpenedEvent(TypedDict, total=True):
    frame: Frame
    """Frame object."""
class frameResizedEvent(TypedDict, total=True):
    pass
class frameStartedNavigatingEvent(TypedDict, total=True):
    frameId: FrameId
    """ID of the frame that is being navigated."""
    url: str
    """The URL the navigation started with. The final URL can be different."""
    loaderId: LoaderId
    """Loader identifier. Even though it is present in case of same-document navigation, the previously committed loaderId would not change unless the navigation changes from a same-document to a cross-document navigation."""
    navigationType: Literal["reload", "reloadBypassingCache", "restore", "restoreWithPost", "historySameDocument", "historyDifferentDocument", "sameDocument", "differentDocument"]
class frameRequestedNavigationEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that is being navigated."""
    reason: ClientNavigationReason
    """The reason for the navigation."""
    url: str
    """The destination URL for the requested navigation."""
    disposition: ClientNavigationDisposition
    """The disposition for the navigation."""
class frameStartedLoadingEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that has started loading."""
class frameStoppedLoadingEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame that has stopped loading."""
class interstitialHiddenEvent(TypedDict, total=True):
    pass
class interstitialShownEvent(TypedDict, total=True):
    pass
class javascriptDialogClosedEvent(TypedDict, total=True):
    frameId: FrameId
    """Frame id."""
    result: bool
    """Whether dialog was confirmed."""
    userInput: str
    """User input in case of prompt."""
class javascriptDialogOpeningEvent(TypedDict, total=True):
    url: str
    """Frame url."""
    frameId: FrameId
    """Frame id."""
    message: str
    """Message that will be displayed by the dialog."""
    type: DialogType
    """Dialog type."""
    hasBrowserHandler: bool
    """True iff browser is capable showing or acting on the given dialog. When browser has no dialog handler for given target, calling alert while Page domain is engaged will stall the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog."""
    defaultPrompt: NotRequired[str]
    """Default dialog prompt."""
class lifecycleEventEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame."""
    loaderId: LoaderId
    """Loader identifier. Empty string if the request is fetched from worker."""
    name: str
    timestamp: MonotonicTime
class backForwardCacheNotUsedEvent(TypedDict, total=True):
    loaderId: LoaderId
    """The loader id for the associated navigation."""
    frameId: FrameId
    """The frame id of the associated frame."""
    notRestoredExplanations: List[BackForwardCacheNotRestoredExplanation]
    """Array of reasons why the page could not be cached. This must not be empty."""
    notRestoredExplanationsTree: NotRequired[BackForwardCacheNotRestoredExplanationTree]
    """Tree structure of reasons why the page could not be cached for each frame."""
class loadEventFiredEvent(TypedDict, total=True):
    timestamp: MonotonicTime
class navigatedWithinDocumentEvent(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame."""
    url: str
    """Frame's new url."""
    navigationType: Literal["fragment", "historyApi", "other"]
    """Navigation type"""
class screencastFrameEvent(TypedDict, total=True):
    data: str
    """Base64-encoded compressed image. (Encoded as a base64 string when passed over JSON)"""
    metadata: ScreencastFrameMetadata
    """Screencast frame metadata."""
    sessionId: int
    """Frame number."""
class screencastVisibilityChangedEvent(TypedDict, total=True):
    visible: bool
    """True if the page is visible."""
class windowOpenEvent(TypedDict, total=True):
    url: str
    """The URL for the new window."""
    windowName: str
    """Window name."""
    windowFeatures: List[str]
    """An array of enabled window features."""
    userGesture: bool
    """Whether or not it was triggered by user gesture."""
class compilationCacheProducedEvent(TypedDict, total=True):
    url: str
    data: str
    """Base64-encoded data (Encoded as a base64 string when passed over JSON)"""