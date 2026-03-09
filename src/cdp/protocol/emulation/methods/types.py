"""CDP Emulation Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import RGBA
    from cdp.protocol.emulation.types import DevicePosture
    from cdp.protocol.emulation.types import DisabledImageType
    from cdp.protocol.emulation.types import DisplayFeature
    from cdp.protocol.emulation.types import MediaFeature
    from cdp.protocol.emulation.types import PressureMetadata
    from cdp.protocol.emulation.types import PressureSource
    from cdp.protocol.emulation.types import PressureState
    from cdp.protocol.emulation.types import SafeAreaInsets
    from cdp.protocol.emulation.types import ScreenId
    from cdp.protocol.emulation.types import ScreenInfo
    from cdp.protocol.emulation.types import ScreenOrientation
    from cdp.protocol.emulation.types import SensorMetadata
    from cdp.protocol.emulation.types import SensorReading
    from cdp.protocol.emulation.types import SensorType
    from cdp.protocol.emulation.types import UserAgentMetadata
    from cdp.protocol.emulation.types import VirtualTimePolicy
    from cdp.protocol.emulation.types import WorkAreaInsets
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.page.types import Viewport




class setFocusEmulationEnabledParameters(TypedDict, total=True):
    enabled: bool
    """Whether to enable to disable focus emulation."""
class setAutoDarkModeOverrideParameters(TypedDict, total=False):
    enabled: NotRequired[bool]
    """Whether to enable or disable automatic dark mode. If not specified, any existing override will be cleared."""
class setCPUThrottlingRateParameters(TypedDict, total=True):
    rate: float
    """Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc)."""
class setDefaultBackgroundColorOverrideParameters(TypedDict, total=False):
    color: NotRequired[RGBA]
    """RGBA of the default background color. If not specified, any existing override will be cleared."""
class setSafeAreaInsetsOverrideParameters(TypedDict, total=True):
    insets: SafeAreaInsets
class setDeviceMetricsOverrideParameters(TypedDict, total=True):
    width: int
    """Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override."""
    height: int
    """Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override."""
    deviceScaleFactor: float
    """Overriding device scale factor value. 0 disables the override."""
    mobile: bool
    """Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more."""
    scale: NotRequired[float]
    """Scale to apply to resulting view image."""
    screenWidth: NotRequired[int]
    """Overriding screen width value in pixels (minimum 0, maximum 10000000)."""
    screenHeight: NotRequired[int]
    """Overriding screen height value in pixels (minimum 0, maximum 10000000)."""
    positionX: NotRequired[int]
    """Overriding view X position on screen in pixels (minimum 0, maximum 10000000)."""
    positionY: NotRequired[int]
    """Overriding view Y position on screen in pixels (minimum 0, maximum 10000000)."""
    dontSetVisibleSize: NotRequired[bool]
    """Do not set visible view size, rely upon explicit setVisibleSize call."""
    screenOrientation: NotRequired[ScreenOrientation]
    """Screen orientation override."""
    viewport: NotRequired[Viewport]
    """If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions."""
    displayFeature: NotRequired[DisplayFeature]
    """If set, the display feature of a multi-segment screen. If not set, multi-segment support is turned-off. Deprecated, use Emulation.setDisplayFeaturesOverride."""
    devicePosture: NotRequired[DevicePosture]
    """If set, the posture of a foldable device. If not set the posture is set to continuous. Deprecated, use Emulation.setDevicePostureOverride."""
    scrollbarType: NotRequired[Literal["overlay", "default"]]
    """Scrollbar type. Default: default."""
    screenOrientationLockEmulation: NotRequired[bool]
    """If set to true, enables screen orientation lock emulation, which intercepts screen.orientation.lock() calls from the page and reports orientation changes via screenOrientationLockChanged events. This is useful for emulating mobile device orientation lock behavior in responsive design mode."""
class setDevicePostureOverrideParameters(TypedDict, total=True):
    posture: DevicePosture

class setDisplayFeaturesOverrideParameters(TypedDict, total=True):
    features: List[DisplayFeature]

class setScrollbarsHiddenParameters(TypedDict, total=True):
    hidden: bool
    """Whether scrollbars should be always hidden."""
class setDocumentCookieDisabledParameters(TypedDict, total=True):
    disabled: bool
    """Whether document.coookie API should be disabled."""
class setEmitTouchEventsForMouseParameters(TypedDict, total=True):
    enabled: bool
    """Whether touch emulation based on mouse input should be enabled."""
    configuration: NotRequired[Literal["mobile", "desktop"]]
    """Touch/gesture events configuration. Default: current platform."""
class setEmulatedMediaParameters(TypedDict, total=False):
    media: NotRequired[str]
    """Media type to emulate. Empty string disables the override."""
    features: NotRequired[List[MediaFeature]]
    """Media features to emulate."""
class setEmulatedVisionDeficiencyParameters(TypedDict, total=True):
    type: Literal["none", "blurredVision", "reducedContrast", "achromatopsia", "deuteranopia", "protanopia", "tritanopia"]
    """Vision deficiency to emulate. Order: best-effort emulations come first, followed by any physiologically accurate emulations for medically recognized color vision deficiencies."""
class setEmulatedOSTextScaleParameters(TypedDict, total=False):
    scale: NotRequired[float]
class setGeolocationOverrideParameters(TypedDict, total=False):
    latitude: NotRequired[float]
    """Mock latitude"""
    longitude: NotRequired[float]
    """Mock longitude"""
    accuracy: NotRequired[float]
    """Mock accuracy"""
    altitude: NotRequired[float]
    """Mock altitude"""
    altitudeAccuracy: NotRequired[float]
    """Mock altitudeAccuracy"""
    heading: NotRequired[float]
    """Mock heading"""
    speed: NotRequired[float]
    """Mock speed"""
class getOverriddenSensorInformationParameters(TypedDict, total=True):
    type: SensorType
class setSensorOverrideEnabledParameters(TypedDict, total=True):
    enabled: bool
    type: SensorType
    metadata: NotRequired[SensorMetadata]
class setSensorOverrideReadingsParameters(TypedDict, total=True):
    type: SensorType
    reading: SensorReading
class setPressureSourceOverrideEnabledParameters(TypedDict, total=True):
    enabled: bool
    source: PressureSource
    metadata: NotRequired[PressureMetadata]
class setPressureStateOverrideParameters(TypedDict, total=True):
    source: PressureSource
    state: PressureState
class setPressureDataOverrideParameters(TypedDict, total=True):
    source: PressureSource
    state: PressureState
    ownContributionEstimate: NotRequired[float]
class setIdleOverrideParameters(TypedDict, total=True):
    isUserActive: bool
    """Mock isUserActive"""
    isScreenUnlocked: bool
    """Mock isScreenUnlocked"""

class setPageScaleFactorParameters(TypedDict, total=True):
    pageScaleFactor: float
    """Page scale factor."""
class setScriptExecutionDisabledParameters(TypedDict, total=True):
    value: bool
    """Whether script execution should be disabled in the page."""
class setTouchEmulationEnabledParameters(TypedDict, total=True):
    enabled: bool
    """Whether the touch event emulation should be enabled."""
    maxTouchPoints: NotRequired[int]
    """Maximum touch points supported. Defaults to one."""
class setVirtualTimePolicyParameters(TypedDict, total=True):
    policy: VirtualTimePolicy
    budget: NotRequired[float]
    """If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent."""
    maxVirtualTimeTaskStarvationCount: NotRequired[int]
    """If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock."""
    initialVirtualTime: NotRequired[TimeSinceEpoch]
    """If set, base::Time::Now will be overridden to initially return this value."""
class setLocaleOverrideParameters(TypedDict, total=False):
    locale: NotRequired[str]
    """ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and restores default host system locale."""
class setTimezoneOverrideParameters(TypedDict, total=True):
    timezoneId: str
    """The timezone identifier. List of supported timezones: https://source.chromium.org/chromium/chromium/deps/icu.git/+/faee8bc70570192d82d2978a71e2a615788597d1:source/data/misc/metaZones.txt If empty, disables the override and restores default host system timezone."""
class setDisabledImageTypesParameters(TypedDict, total=True):
    imageTypes: List[DisabledImageType]
    """Image types to disable."""
class setDataSaverOverrideParameters(TypedDict, total=False):
    dataSaverEnabled: NotRequired[bool]
    """Override value. Omitting the parameter disables the override."""
class setHardwareConcurrencyOverrideParameters(TypedDict, total=True):
    hardwareConcurrency: int
    """Hardware concurrency to report"""
class setUserAgentOverrideParameters(TypedDict, total=True):
    userAgent: str
    """User agent to use."""
    acceptLanguage: NotRequired[str]
    """Browser language to emulate."""
    platform: NotRequired[str]
    """The platform navigator.platform should return."""
    userAgentMetadata: NotRequired[UserAgentMetadata]
    """To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData"""
class setAutomationOverrideParameters(TypedDict, total=True):
    enabled: bool
    """Whether the override should be enabled."""
class setSmallViewportHeightDifferenceOverrideParameters(TypedDict, total=True):
    difference: int
    """This will cause an element of size 100svh to be difference pixels smaller than an element of size 100lvh."""

class addScreenParameters(TypedDict, total=True):
    left: int
    """Offset of the left edge of the screen in pixels."""
    top: int
    """Offset of the top edge of the screen in pixels."""
    width: int
    """The width of the screen in pixels."""
    height: int
    """The height of the screen in pixels."""
    workAreaInsets: NotRequired[WorkAreaInsets]
    """Specifies the screen's work area. Default is entire screen."""
    devicePixelRatio: NotRequired[float]
    """Specifies the screen's device pixel ratio. Default is 1."""
    rotation: NotRequired[int]
    """Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270. Default is 0."""
    colorDepth: NotRequired[int]
    """Specifies the screen's color depth in bits. Default is 24."""
    label: NotRequired[str]
    """Specifies the descriptive label for the screen. Default is none."""
    isInternal: NotRequired[bool]
    """Indicates whether the screen is internal to the device or external, attached to the device. Default is false."""
class updateScreenParameters(TypedDict, total=True):
    screenId: ScreenId
    """Target screen identifier."""
    left: NotRequired[int]
    """Offset of the left edge of the screen in pixels."""
    top: NotRequired[int]
    """Offset of the top edge of the screen in pixels."""
    width: NotRequired[int]
    """The width of the screen in pixels."""
    height: NotRequired[int]
    """The height of the screen in pixels."""
    workAreaInsets: NotRequired[WorkAreaInsets]
    """Specifies the screen's work area."""
    devicePixelRatio: NotRequired[float]
    """Specifies the screen's device pixel ratio."""
    rotation: NotRequired[int]
    """Specifies the screen's rotation angle. Available values are 0, 90, 180 and 270."""
    colorDepth: NotRequired[int]
    """Specifies the screen's color depth in bits."""
    label: NotRequired[str]
    """Specifies the descriptive label for the screen."""
    isInternal: NotRequired[bool]
    """Indicates whether the screen is internal to the device or external, attached to the device. Default is false."""
class removeScreenParameters(TypedDict, total=True):
    screenId: ScreenId
class setPrimaryScreenParameters(TypedDict, total=True):
    screenId: ScreenId




















class getOverriddenSensorInformationReturns(TypedDict):
    requestedSamplingFrequency: float










class setVirtualTimePolicyReturns(TypedDict):
    virtualTimeTicksBase: float
    """Absolute timestamp at which virtual time was first enabled (up time in milliseconds)."""








class getScreenInfosReturns(TypedDict):
    screenInfos: List[ScreenInfo]
class addScreenReturns(TypedDict):
    screenInfo: ScreenInfo
class updateScreenReturns(TypedDict):
    screenInfo: ScreenInfo