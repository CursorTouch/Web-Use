"""CDP PWA Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.pwa.types import DisplayMode
    from cdp.protocol.pwa.types import FileHandler
    from cdp.protocol.target.types import TargetID

class getOsAppStateParameters(TypedDict, total=True):
    manifestId: str
    """The id from the webapp's manifest file, commonly it's the url of the site installing the webapp. See https://web.dev/learn/pwa/web-app-manifest."""
class installParameters(TypedDict, total=True):
    manifestId: str
    installUrlOrBundleUrl: NotRequired[str]
    """The location of the app or bundle overriding the one derived from the manifestId."""
class uninstallParameters(TypedDict, total=True):
    manifestId: str
class launchParameters(TypedDict, total=True):
    manifestId: str
    url: NotRequired[str]
class launchFilesInAppParameters(TypedDict, total=True):
    manifestId: str
    files: List[str]
class openCurrentPageInAppParameters(TypedDict, total=True):
    manifestId: str
class changeAppUserSettingsParameters(TypedDict, total=True):
    manifestId: str
    linkCapturing: NotRequired[bool]
    """If user allows the links clicked on by the user in the app's scope, or extended scope if the manifest has scope extensions and the flags DesktopPWAsLinkCapturingWithScopeExtensions and WebAppEnableScopeExtensions are enabled.  Note, the API does not support resetting the linkCapturing to the initial value, uninstalling and installing the web app again will reset it.  TODO(crbug.com/339453269): Setting this value on ChromeOS is not supported yet."""
    displayMode: NotRequired[DisplayMode]
class getOsAppStateReturns(TypedDict):
    badgeCount: int
    fileHandlers: List[FileHandler]


class launchReturns(TypedDict):
    targetId: TargetID
    """ID of the tab target created as a result."""
class launchFilesInAppReturns(TypedDict):
    targetIds: List[TargetID]
    """IDs of the tab targets created as the result."""