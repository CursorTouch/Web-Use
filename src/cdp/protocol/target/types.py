"""CDP Target Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.browser.types import BrowserContextID
    from cdp.protocol.page.types import FrameId

TargetID = str
SessionID = str
"""Unique identifier of attached debugging session."""
class TargetInfo(TypedDict, total=True):
    targetId: TargetID
    type: str
    """List of types: https://source.chromium.org/chromium/chromium/src/+/main:content/browser/devtools/devtools_agent_host_impl.cc?ss=chromium&q=f:devtools%20-f:out%20%22::kTypeTab%5B%5D%22"""
    title: str
    url: str
    attached: bool
    """Whether the target has an attached client."""
    canAccessOpener: bool
    """Whether the target has access to the originating window."""
    openerId: NotRequired[TargetID]
    """Opener target Id"""
    openerFrameId: NotRequired[FrameId]
    """Frame id of originating window (is only set if target has an opener)."""
    parentFrameId: NotRequired[FrameId]
    """Id of the parent frame, only present for the "iframe" targets."""
    browserContextId: NotRequired[BrowserContextID]
    subtype: NotRequired[str]
    """Provides additional details for specific target types. For example, for the type of "page", this may be set to "prerender"."""
class FilterEntry(TypedDict, total=False):
    """A filter used by target query/discovery/auto-attach operations."""
    exclude: NotRequired[bool]
    """If set, causes exclusion of matching targets from the list."""
    type: NotRequired[str]
    """If not present, matches any type."""
TargetFilter = List[FilterEntry]
"""The entries in TargetFilter are matched sequentially against targets and the first entry that matches determines if the target is included or not, depending on the value of exclude field in the entry. If filter is not specified, the one assumed is [{type: "browser", exclude: true}, {type: "tab", exclude: true}, {}] (i.e. include everything but browser and tab)."""
class RemoteLocation(TypedDict, total=True):
    host: str
    port: int
WindowState = Literal['normal','minimized','maximized','fullscreen']
"""The state of the target window."""