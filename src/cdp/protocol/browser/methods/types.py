"""CDP Browser Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.browser.types import Bounds
    from cdp.protocol.browser.types import BrowserCommandId
    from cdp.protocol.browser.types import BrowserContextID
    from cdp.protocol.browser.types import Histogram
    from cdp.protocol.browser.types import PermissionDescriptor
    from cdp.protocol.browser.types import PermissionSetting
    from cdp.protocol.browser.types import PrivacySandboxAPI
    from cdp.protocol.browser.types import WindowID
    from cdp.protocol.target.types import TargetID

class setPermissionParameters(TypedDict, total=True):
    permission: PermissionDescriptor
    """Descriptor of permission to override."""
    setting: PermissionSetting
    """Setting of the permission."""
    origin: NotRequired[str]
    """Embedding origin the permission applies to, all origins if not specified."""
    embeddedOrigin: NotRequired[str]
    """Embedded origin the permission applies to. It is ignored unless the embedding origin is present and valid. If the embedding origin is provided but the embedded origin isn't, the embedding origin is used as the embedded origin."""
    browserContextId: NotRequired[BrowserContextID]
    """Context to override. When omitted, default browser context is used."""
class resetPermissionsParameters(TypedDict, total=False):
    browserContextId: NotRequired[BrowserContextID]
    """BrowserContext to reset permissions. When omitted, default browser context is used."""
class setDownloadBehaviorParameters(TypedDict, total=True):
    behavior: Literal["deny", "allow", "allowAndName", "default"]
    """Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny). |allowAndName| allows download and names files according to their download guids."""
    browserContextId: NotRequired[BrowserContextID]
    """BrowserContext to set download behavior. When omitted, default browser context is used."""
    downloadPath: NotRequired[str]
    """The default path to save downloaded files to. This is required if behavior is set to 'allow' or 'allowAndName'."""
    eventsEnabled: NotRequired[bool]
    """Whether to emit download events (defaults to false)."""
class cancelDownloadParameters(TypedDict, total=True):
    guid: str
    """Global unique identifier of the download."""
    browserContextId: NotRequired[BrowserContextID]
    """BrowserContext to perform the action in. When omitted, default browser context is used."""





class getHistogramsParameters(TypedDict, total=False):
    query: NotRequired[str]
    """Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms."""
    delta: NotRequired[bool]
    """If true, retrieve delta since last delta call."""
class getHistogramParameters(TypedDict, total=True):
    name: str
    """Requested histogram name."""
    delta: NotRequired[bool]
    """If true, retrieve delta since last delta call."""
class getWindowBoundsParameters(TypedDict, total=True):
    windowId: WindowID
    """Browser window id."""
class getWindowForTargetParameters(TypedDict, total=False):
    targetId: NotRequired[TargetID]
    """Devtools agent host id. If called as a part of the session, associated targetId is used."""
class setWindowBoundsParameters(TypedDict, total=True):
    windowId: WindowID
    """Browser window id."""
    bounds: Bounds
    """New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged."""
class setContentsSizeParameters(TypedDict, total=True):
    windowId: WindowID
    """Browser window id."""
    width: NotRequired[int]
    """The window contents width in DIP. Assumes current width if omitted. Must be specified if 'height' is omitted."""
    height: NotRequired[int]
    """The window contents height in DIP. Assumes current height if omitted. Must be specified if 'width' is omitted."""
class setDockTileParameters(TypedDict, total=False):
    badgeLabel: NotRequired[str]
    image: NotRequired[str]
    """Png encoded image. (Encoded as a base64 string when passed over JSON)"""
class executeBrowserCommandParameters(TypedDict, total=True):
    commandId: BrowserCommandId
class addPrivacySandboxEnrollmentOverrideParameters(TypedDict, total=True):
    url: str
class addPrivacySandboxCoordinatorKeyConfigParameters(TypedDict, total=True):
    api: PrivacySandboxAPI
    coordinatorOrigin: str
    keyConfig: str
    browserContextId: NotRequired[BrowserContextID]
    """BrowserContext to perform the action in. When omitted, default browser context is used."""







class getVersionReturns(TypedDict):
    protocolVersion: str
    """Protocol version."""
    product: str
    """Product name."""
    revision: str
    """Product revision."""
    userAgent: str
    """User-Agent."""
    jsVersion: str
    """V8 version."""
class getBrowserCommandLineReturns(TypedDict):
    arguments: List[str]
    """Commandline parameters"""
class getHistogramsReturns(TypedDict):
    histograms: List[Histogram]
    """Histograms."""
class getHistogramReturns(TypedDict):
    histogram: Histogram
    """Histogram."""
class getWindowBoundsReturns(TypedDict):
    bounds: Bounds
    """Bounds information of the window. When window state is 'minimized', the restored window position and size are returned."""
class getWindowForTargetReturns(TypedDict):
    windowId: WindowID
    """Browser window id."""
    bounds: Bounds
    """Bounds information of the window. When window state is 'minimized', the restored window position and size are returned."""