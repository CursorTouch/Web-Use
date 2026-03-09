"""CDP Browser Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

BrowserContextID = str
WindowID = int
WindowState = Literal['normal','minimized','maximized','fullscreen']
"""The state of the browser window."""
class Bounds(TypedDict, total=False):
    """Browser window bounds information"""
    left: NotRequired[int]
    """The offset from the left edge of the screen to the window in pixels."""
    top: NotRequired[int]
    """The offset from the top edge of the screen to the window in pixels."""
    width: NotRequired[int]
    """The window width in pixels."""
    height: NotRequired[int]
    """The window height in pixels."""
    windowState: NotRequired[WindowState]
    """The window state. Default to normal."""
PermissionType = Literal['ar','audioCapture','automaticFullscreen','backgroundFetch','backgroundSync','cameraPanTiltZoom','capturedSurfaceControl','clipboardReadWrite','clipboardSanitizedWrite','displayCapture','durableStorage','geolocation','handTracking','idleDetection','keyboardLock','localFonts','localNetwork','localNetworkAccess','loopbackNetwork','midi','midiSysex','nfc','notifications','paymentHandler','periodicBackgroundSync','pointerLock','protectedMediaIdentifier','sensors','smartCard','speakerSelection','storageAccess','topLevelStorageAccess','videoCapture','vr','wakeLockScreen','wakeLockSystem','webAppInstallation','webPrinting','windowManagement']
PermissionSetting = Literal['granted','denied','prompt']
class PermissionDescriptor(TypedDict, total=True):
    """Definition of PermissionDescriptor defined in the Permissions API: https://w3c.github.io/permissions/#dom-permissiondescriptor."""
    name: str
    """Name of permission. See https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl for valid permission names."""
    sysex: NotRequired[bool]
    """For "midi" permission, may also specify sysex control."""
    userVisibleOnly: NotRequired[bool]
    """For "push" permission, may specify userVisibleOnly. Note that userVisibleOnly = true is the only currently supported type."""
    allowWithoutSanitization: NotRequired[bool]
    """For "clipboard" permission, may specify allowWithoutSanitization."""
    allowWithoutGesture: NotRequired[bool]
    """For "fullscreen" permission, must specify allowWithoutGesture:true."""
    panTiltZoom: NotRequired[bool]
    """For "camera" permission, may specify panTiltZoom."""
BrowserCommandId = Literal['openTabSearch','closeTabSearch','openGlic']
"""Browser command ids used by executeBrowserCommand."""
class Bucket(TypedDict, total=True):
    """Chrome histogram bucket."""
    low: int
    """Minimum value (inclusive)."""
    high: int
    """Maximum value (exclusive)."""
    count: int
    """Number of samples."""
class Histogram(TypedDict, total=True):
    """Chrome histogram."""
    name: str
    """Name."""
    sum: int
    """Sum of sample values."""
    count: int
    """Total number of samples."""
    buckets: List[Bucket]
    """Buckets."""
PrivacySandboxAPI = Literal['BiddingAndAuctionServices','TrustedKeyValue']