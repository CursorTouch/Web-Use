"""CDP Emulation Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

class SafeAreaInsets(TypedDict, total=False):
    top: NotRequired[int]
    """Overrides safe-area-inset-top."""
    topMax: NotRequired[int]
    """Overrides safe-area-max-inset-top."""
    left: NotRequired[int]
    """Overrides safe-area-inset-left."""
    leftMax: NotRequired[int]
    """Overrides safe-area-max-inset-left."""
    bottom: NotRequired[int]
    """Overrides safe-area-inset-bottom."""
    bottomMax: NotRequired[int]
    """Overrides safe-area-max-inset-bottom."""
    right: NotRequired[int]
    """Overrides safe-area-inset-right."""
    rightMax: NotRequired[int]
    """Overrides safe-area-max-inset-right."""
class ScreenOrientation(TypedDict, total=True):
    """Screen orientation."""
    type: Literal["portraitPrimary", "portraitSecondary", "landscapePrimary", "landscapeSecondary"]
    """Orientation type."""
    angle: int
    """Orientation angle."""
class DisplayFeature(TypedDict, total=True):
    orientation: Literal["vertical", "horizontal"]
    """Orientation of a display feature in relation to screen"""
    offset: int
    """The offset from the screen origin in either the x (for vertical orientation) or y (for horizontal orientation) direction."""
    maskLength: int
    """A display feature may mask content such that it is not physically displayed - this length along with the offset describes this area. A display feature that only splits content will have a 0 mask_length."""
class DevicePosture(TypedDict, total=True):
    type: Literal["continuous", "folded"]
    """Current posture of the device"""
class MediaFeature(TypedDict, total=True):
    name: str
    value: str
VirtualTimePolicy = Literal['advance','pause','pauseIfNetworkFetchesPending']
"""advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches."""
class UserAgentBrandVersion(TypedDict, total=True):
    """Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints"""
    brand: str
    version: str
class UserAgentMetadata(TypedDict, total=True):
    """Used to specify User Agent Client Hints to emulate. See https://wicg.github.io/ua-client-hints Missing optional values will be filled in by the target with what it would normally use."""
    platform: str
    platformVersion: str
    architecture: str
    model: str
    mobile: bool
    brands: NotRequired[List[UserAgentBrandVersion]]
    """Brands appearing in Sec-CH-UA."""
    fullVersionList: NotRequired[List[UserAgentBrandVersion]]
    """Brands appearing in Sec-CH-UA-Full-Version-List."""
    bitness: NotRequired[str]
    wow64: NotRequired[bool]
    formFactors: NotRequired[List[str]]
    """Used to specify User Agent form-factor values. See https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factors"""
SensorType = Literal['absolute-orientation','accelerometer','ambient-light','gravity','gyroscope','linear-acceleration','magnetometer','relative-orientation']
"""Used to specify sensor types to emulate. See https://w3c.github.io/sensors/#automation for more information."""
class SensorMetadata(TypedDict, total=False):
    available: NotRequired[bool]
    minimumFrequency: NotRequired[float]
    maximumFrequency: NotRequired[float]
class SensorReadingSingle(TypedDict, total=True):
    value: float
class SensorReadingXYZ(TypedDict, total=True):
    x: float
    y: float
    z: float
class SensorReadingQuaternion(TypedDict, total=True):
    x: float
    y: float
    z: float
    w: float
class SensorReading(TypedDict, total=False):
    single: NotRequired[SensorReadingSingle]
    xyz: NotRequired[SensorReadingXYZ]
    quaternion: NotRequired[SensorReadingQuaternion]
PressureSource = Literal['cpu']
PressureState = Literal['nominal','fair','serious','critical']
class PressureMetadata(TypedDict, total=False):
    available: NotRequired[bool]
class WorkAreaInsets(TypedDict, total=False):
    top: NotRequired[int]
    """Work area top inset in pixels. Default is 0;"""
    left: NotRequired[int]
    """Work area left inset in pixels. Default is 0;"""
    bottom: NotRequired[int]
    """Work area bottom inset in pixels. Default is 0;"""
    right: NotRequired[int]
    """Work area right inset in pixels. Default is 0;"""
ScreenId = str
class ScreenInfo(TypedDict, total=True):
    """Screen information similar to the one returned by window.getScreenDetails() method, see https://w3c.github.io/window-management/#screendetailed."""
    left: int
    """Offset of the left edge of the screen."""
    top: int
    """Offset of the top edge of the screen."""
    width: int
    """Width of the screen."""
    height: int
    """Height of the screen."""
    availLeft: int
    """Offset of the left edge of the available screen area."""
    availTop: int
    """Offset of the top edge of the available screen area."""
    availWidth: int
    """Width of the available screen area."""
    availHeight: int
    """Height of the available screen area."""
    devicePixelRatio: float
    """Specifies the screen's device pixel ratio."""
    orientation: ScreenOrientation
    """Specifies the screen's orientation."""
    colorDepth: int
    """Specifies the screen's color depth in bits."""
    isExtended: bool
    """Indicates whether the device has multiple screens."""
    isInternal: bool
    """Indicates whether the screen is internal to the device or external, attached to the device."""
    isPrimary: bool
    """Indicates whether the screen is set as the the operating system primary screen."""
    label: str
    """Specifies the descriptive label for the screen."""
    id: ScreenId
    """Specifies the unique identifier of the screen."""
DisabledImageType = Literal['avif','jxl','webp']
"""Enum of image types that can be disabled."""