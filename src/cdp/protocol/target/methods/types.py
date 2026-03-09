"""CDP Target Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.browser.types import BrowserContextID
    from cdp.protocol.target.types import RemoteLocation
    from cdp.protocol.target.types import SessionID
    from cdp.protocol.target.types import TargetFilter
    from cdp.protocol.target.types import TargetID
    from cdp.protocol.target.types import TargetInfo
    from cdp.protocol.target.types import WindowState

class activateTargetParameters(TypedDict, total=True):
    targetId: TargetID
class attachToTargetParameters(TypedDict, total=True):
    targetId: TargetID
    flatten: NotRequired[bool]
    """Enables "flat" access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325."""

class closeTargetParameters(TypedDict, total=True):
    targetId: TargetID
class exposeDevToolsProtocolParameters(TypedDict, total=True):
    targetId: TargetID
    bindingName: NotRequired[str]
    """Binding name, 'cdp' if not specified."""
    inheritPermissions: NotRequired[bool]
    """If true, inherits the current root session's permissions (default: false)."""
class createBrowserContextParameters(TypedDict, total=False):
    disposeOnDetach: NotRequired[bool]
    """If specified, disposes this context when debugging session disconnects."""
    proxyServer: NotRequired[str]
    """Proxy server, similar to the one passed to --proxy-server"""
    proxyBypassList: NotRequired[str]
    """Proxy bypass list, similar to the one passed to --proxy-bypass-list"""
    originsWithUniversalNetworkAccess: NotRequired[List[str]]
    """An optional list of origins to grant unlimited cross-origin access to. Parts of the URL other than those constituting origin are ignored."""

class createTargetParameters(TypedDict, total=True):
    url: str
    """The initial URL the page will be navigated to. An empty string indicates about:blank."""
    left: NotRequired[int]
    """Frame left origin in DIP (requires newWindow to be true or headless shell)."""
    top: NotRequired[int]
    """Frame top origin in DIP (requires newWindow to be true or headless shell)."""
    width: NotRequired[int]
    """Frame width in DIP (requires newWindow to be true or headless shell)."""
    height: NotRequired[int]
    """Frame height in DIP (requires newWindow to be true or headless shell)."""
    windowState: NotRequired[WindowState]
    """Frame window state (requires newWindow to be true or headless shell). Default is normal."""
    browserContextId: NotRequired[BrowserContextID]
    """The browser context to create the page in."""
    enableBeginFrameControl: NotRequired[bool]
    """Whether BeginFrames for this target will be controlled via DevTools (headless shell only, not supported on MacOS yet, false by default)."""
    newWindow: NotRequired[bool]
    """Whether to create a new Window or Tab (false by default, not supported by headless shell)."""
    background: NotRequired[bool]
    """Whether to create the target in background or foreground (false by default, not supported by headless shell)."""
    forTab: NotRequired[bool]
    """Whether to create the target of type "tab"."""
    hidden: NotRequired[bool]
    """Whether to create a hidden target. The hidden target is observable via protocol, but not present in the tab UI strip. Cannot be created with forTab: true, newWindow: true or background: false. The life-time of the tab is limited to the life-time of the session."""
    focus: NotRequired[bool]
    """If specified, the option is used to determine if the new target should be focused or not. By default, the focus behavior depends on the value of the background field. For example, background=false and focus=false will result in the target tab being opened but the browser window remain unchanged (if it was in the background, it will remain in the background) and background=false with focus=undefined will result in the window being focused. Using background: true and focus: true is not supported and will result in an error."""
class detachFromTargetParameters(TypedDict, total=False):
    sessionId: NotRequired[SessionID]
    """Session to detach."""
    targetId: NotRequired[TargetID]
    """Deprecated."""
class disposeBrowserContextParameters(TypedDict, total=True):
    browserContextId: BrowserContextID
class getTargetInfoParameters(TypedDict, total=False):
    targetId: NotRequired[TargetID]
class getTargetsParameters(TypedDict, total=False):
    filter: NotRequired[TargetFilter]
    """Only targets matching filter will be reported. If filter is not specified and target discovery is currently enabled, a filter used for target discovery is used for consistency."""
class setAutoAttachParameters(TypedDict, total=True):
    autoAttach: bool
    """Whether to auto-attach to related targets."""
    waitForDebuggerOnStart: bool
    """Whether to pause new targets when attaching to them. Use Runtime.runIfWaitingForDebugger to run paused targets."""
    flatten: NotRequired[bool]
    """Enables "flat" access to the session via specifying sessionId attribute in the commands. We plan to make this the default, deprecate non-flattened mode, and eventually retire it. See crbug.com/991325."""
    filter: NotRequired[TargetFilter]
    """Only targets matching filter will be attached."""
class autoAttachRelatedParameters(TypedDict, total=True):
    targetId: TargetID
    waitForDebuggerOnStart: bool
    """Whether to pause new targets when attaching to them. Use Runtime.runIfWaitingForDebugger to run paused targets."""
    filter: NotRequired[TargetFilter]
    """Only targets matching filter will be attached."""
class setDiscoverTargetsParameters(TypedDict, total=True):
    discover: bool
    """Whether to discover available targets."""
    filter: NotRequired[TargetFilter]
    """Only targets matching filter will be attached. If discover is false, filter must be omitted or empty."""
class setRemoteLocationsParameters(TypedDict, total=True):
    locations: List[RemoteLocation]
    """List of remote locations."""
class getDevToolsTargetParameters(TypedDict, total=True):
    targetId: TargetID
    """Page or tab target ID."""
class openDevToolsParameters(TypedDict, total=True):
    targetId: TargetID
    """This can be the page or tab target ID."""
    panelId: NotRequired[str]
    """The id of the panel we want DevTools to open initially. Currently supported panels are elements, console, network, sources, resources and performance."""

class attachToTargetReturns(TypedDict):
    sessionId: SessionID
    """Id assigned to the session."""
class attachToBrowserTargetReturns(TypedDict):
    sessionId: SessionID
    """Id assigned to the session."""
class closeTargetReturns(TypedDict):
    success: bool
    """Always set to true. If an error occurs, the response indicates protocol error."""

class createBrowserContextReturns(TypedDict):
    browserContextId: BrowserContextID
    """The id of the context created."""
class getBrowserContextsReturns(TypedDict):
    browserContextIds: List[BrowserContextID]
    """An array of browser context ids."""
    defaultBrowserContextId: BrowserContextID
    """The id of the default browser context if available."""
class createTargetReturns(TypedDict):
    targetId: TargetID
    """The id of the page opened."""


class getTargetInfoReturns(TypedDict):
    targetInfo: TargetInfo
class getTargetsReturns(TypedDict):
    targetInfos: List[TargetInfo]
    """The list of targets."""




class getDevToolsTargetReturns(TypedDict):
    targetId: TargetID
    """The targetId of DevTools page target if exists."""
class openDevToolsReturns(TypedDict):
    targetId: TargetID
    """The targetId of DevTools page target."""