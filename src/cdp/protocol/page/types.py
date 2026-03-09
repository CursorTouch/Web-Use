"""CDP Page Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.network.types import ResourceType
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.runtime.types import ScriptId
    from cdp.protocol.runtime.types import UniqueDebuggerId

FrameId = str
"""Unique frame identifier."""
AdFrameType = Literal['none','child','root']
"""Indicates whether a frame has been identified as an ad."""
AdFrameExplanation = Literal['ParentIsAd','CreatedByAdScript','MatchedBlockingRule']
class AdFrameStatus(TypedDict, total=True):
    """Indicates whether a frame has been identified as an ad and why."""
    adFrameType: AdFrameType
    explanations: NotRequired[List[AdFrameExplanation]]
class AdScriptId(TypedDict, total=True):
    """Identifies the script which caused a script or frame to be labelled as an ad."""
    scriptId: ScriptId
    """Script Id of the script which caused a script or frame to be labelled as an ad."""
    debuggerId: UniqueDebuggerId
    """Id of scriptId's debugger."""
class AdScriptAncestry(TypedDict, total=True):
    """Encapsulates the script ancestry and the root script filterlist rule that caused the frame to be labelled as an ad. Only created when ancestryChain is not empty."""
    ancestryChain: List[AdScriptId]
    """A chain of AdScriptIds representing the ancestry of an ad script that led to the creation of a frame. The chain is ordered from the script itself (lower level) up to its root ancestor that was flagged by filterlist."""
    rootScriptFilterlistRule: NotRequired[str]
    """The filterlist rule that caused the root (last) script in ancestryChain to be ad-tagged. Only populated if the rule is available."""
SecureContextType = Literal['Secure','SecureLocalhost','InsecureScheme','InsecureAncestor']
"""Indicates whether the frame is a secure context and why it is the case."""
CrossOriginIsolatedContextType = Literal['Isolated','NotIsolated','NotIsolatedFeatureDisabled']
"""Indicates whether the frame is cross-origin isolated and why it is the case."""
GatedAPIFeatures = Literal['SharedArrayBuffers','SharedArrayBuffersTransferAllowed','PerformanceMeasureMemory','PerformanceProfile']
PermissionsPolicyFeature = Literal['accelerometer','all-screens-capture','ambient-light-sensor','aria-notify','attribution-reporting','autofill','autoplay','bluetooth','browsing-topics','camera','captured-surface-control','ch-dpr','ch-device-memory','ch-downlink','ch-ect','ch-prefers-color-scheme','ch-prefers-reduced-motion','ch-prefers-reduced-transparency','ch-rtt','ch-save-data','ch-ua','ch-ua-arch','ch-ua-bitness','ch-ua-high-entropy-values','ch-ua-platform','ch-ua-model','ch-ua-mobile','ch-ua-form-factors','ch-ua-full-version','ch-ua-full-version-list','ch-ua-platform-version','ch-ua-wow64','ch-viewport-height','ch-viewport-width','ch-width','clipboard-read','clipboard-write','compute-pressure','controlled-frame','cross-origin-isolated','deferred-fetch','deferred-fetch-minimal','device-attributes','digital-credentials-create','digital-credentials-get','direct-sockets','direct-sockets-multicast','direct-sockets-private','display-capture','document-domain','encrypted-media','execution-while-out-of-viewport','execution-while-not-rendered','fenced-unpartitioned-storage-read','focus-without-user-activation','fullscreen','frobulate','gamepad','geolocation','gyroscope','hid','identity-credentials-get','idle-detection','interest-cohort','join-ad-interest-group','keyboard-map','language-detector','language-model','local-fonts','local-network','local-network-access','loopback-network','magnetometer','manual-text','media-playback-while-not-visible','microphone','midi','on-device-speech-recognition','otp-credentials','payment','picture-in-picture','private-aggregation','private-state-token-issuance','private-state-token-redemption','publickey-credentials-create','publickey-credentials-get','record-ad-auction-events','rewriter','run-ad-auction','screen-wake-lock','serial','shared-storage','shared-storage-select-url','smart-card','speaker-selection','storage-access','sub-apps','summarizer','sync-xhr','translator','unload','usb','usb-unrestricted','vertical-scroll','web-app-installation','web-printing','web-share','window-management','writer','xr-spatial-tracking']
"""All Permissions Policy features. This enum should match the one defined in services/network/public/cpp/permissions_policy/permissions_policy_features.json5. LINT.IfChange(PermissionsPolicyFeature)"""
PermissionsPolicyBlockReason = Literal['Header','IframeAttribute','InFencedFrameTree','InIsolatedApp']
"""Reason for a permissions policy feature to be disabled."""
class PermissionsPolicyBlockLocator(TypedDict, total=True):
    frameId: FrameId
    blockReason: PermissionsPolicyBlockReason
class PermissionsPolicyFeatureState(TypedDict, total=True):
    feature: PermissionsPolicyFeature
    allowed: bool
    locator: NotRequired[PermissionsPolicyBlockLocator]
OriginTrialTokenStatus = Literal['Success','NotSupported','Insecure','Expired','WrongOrigin','InvalidSignature','Malformed','WrongVersion','FeatureDisabled','TokenDisabled','FeatureDisabledForUser','UnknownTrial']
"""Origin Trial(https://www.chromium.org/blink/origin-trials) support. Status for an Origin Trial token."""
OriginTrialStatus = Literal['Enabled','ValidTokenNotProvided','OSNotSupported','TrialNotAllowed']
"""Status for an Origin Trial."""
OriginTrialUsageRestriction = Literal['None','Subset']
class OriginTrialToken(TypedDict, total=True):
    origin: str
    matchSubDomains: bool
    trialName: str
    expiryTime: TimeSinceEpoch
    isThirdParty: bool
    usageRestriction: OriginTrialUsageRestriction
class OriginTrialTokenWithStatus(TypedDict, total=True):
    rawTokenText: str
    status: OriginTrialTokenStatus
    parsedToken: NotRequired[OriginTrialToken]
    """parsedToken is present only when the token is extractable and parsable."""
class OriginTrial(TypedDict, total=True):
    trialName: str
    status: OriginTrialStatus
    tokensWithStatus: List[OriginTrialTokenWithStatus]
class SecurityOriginDetails(TypedDict, total=True):
    """Additional information about the frame document's security origin."""
    isLocalhost: bool
    """Indicates whether the frame document's security origin is one of the local hostnames (e.g. localhost) or IP addresses (IPv4 127.0.0.0/8 or IPv6 ::1)."""
class Frame(TypedDict, total=True):
    """Information about the Frame on the page."""
    id: FrameId
    """Frame unique identifier."""
    loaderId: LoaderId
    """Identifier of the loader associated with this frame."""
    url: str
    """Frame document's URL without fragment."""
    domainAndRegistry: str
    """Frame document's registered domain, taking the public suffixes list into account. Extracted from the Frame's url. Example URLs: http://www.google.com/file.html -> google.com               http://a.b.co.uk/file.html      -> b.co.uk"""
    securityOrigin: str
    """Frame document's security origin."""
    mimeType: str
    """Frame document's mimeType as determined by the browser."""
    secureContextType: SecureContextType
    """Indicates whether the main document is a secure context and explains why that is the case."""
    crossOriginIsolatedContextType: CrossOriginIsolatedContextType
    """Indicates whether this is a cross origin isolated context."""
    gatedAPIFeatures: List[GatedAPIFeatures]
    """Indicated which gated APIs / features are available."""
    parentId: NotRequired[FrameId]
    """Parent frame identifier."""
    name: NotRequired[str]
    """Frame's name as specified in the tag."""
    urlFragment: NotRequired[str]
    """Frame document's URL fragment including the '#'."""
    securityOriginDetails: NotRequired[SecurityOriginDetails]
    """Additional details about the frame document's security origin."""
    unreachableUrl: NotRequired[str]
    """If the frame failed to load, this contains the URL that could not be loaded. Note that unlike url above, this URL may contain a fragment."""
    adFrameStatus: NotRequired[AdFrameStatus]
    """Indicates whether this frame was tagged as an ad and why."""
class FrameResource(TypedDict, total=True):
    """Information about the Resource on the page."""
    url: str
    """Resource URL."""
    type: ResourceType
    """Type of this resource."""
    mimeType: str
    """Resource mimeType as determined by the browser."""
    lastModified: NotRequired[TimeSinceEpoch]
    """last-modified timestamp as reported by server."""
    contentSize: NotRequired[float]
    """Resource content size."""
    failed: NotRequired[bool]
    """True if the resource failed to load."""
    canceled: NotRequired[bool]
    """True if the resource was canceled during loading."""
class FrameResourceTree(TypedDict, total=True):
    """Information about the Frame hierarchy along with their cached resources."""
    frame: Frame
    """Frame information for this tree item."""
    resources: List[FrameResource]
    """Information about frame resources."""
    childFrames: NotRequired[List[FrameResourceTree]]
    """Child frames."""
class FrameTree(TypedDict, total=True):
    """Information about the Frame hierarchy."""
    frame: Frame
    """Frame information for this tree item."""
    childFrames: NotRequired[List[FrameTree]]
    """Child frames."""
ScriptIdentifier = str
"""Unique script identifier."""
TransitionType = Literal['link','typed','address_bar','auto_bookmark','auto_subframe','manual_subframe','generated','auto_toplevel','form_submit','reload','keyword','keyword_generated','other']
"""Transition type."""
class NavigationEntry(TypedDict, total=True):
    """Navigation history entry."""
    id: int
    """Unique id of the navigation history entry."""
    url: str
    """URL of the navigation history entry."""
    userTypedURL: str
    """URL that the user typed in the url bar."""
    title: str
    """Title of the navigation history entry."""
    transitionType: TransitionType
    """Transition type."""
class ScreencastFrameMetadata(TypedDict, total=True):
    """Screencast frame metadata."""
    offsetTop: float
    """Top offset in DIP."""
    pageScaleFactor: float
    """Page scale factor."""
    deviceWidth: float
    """Device screen width in DIP."""
    deviceHeight: float
    """Device screen height in DIP."""
    scrollOffsetX: float
    """Position of horizontal scroll in CSS pixels."""
    scrollOffsetY: float
    """Position of vertical scroll in CSS pixels."""
    timestamp: NotRequired[TimeSinceEpoch]
    """Frame swap timestamp."""
DialogType = Literal['alert','confirm','prompt','beforeunload']
"""Javascript dialog type."""
class AppManifestError(TypedDict, total=True):
    """Error while paring app manifest."""
    message: str
    """Error message."""
    critical: int
    """If critical, this is a non-recoverable parse error."""
    line: int
    """Error line."""
    column: int
    """Error column."""
class AppManifestParsedProperties(TypedDict, total=True):
    """Parsed app manifest properties."""
    scope: str
    """Computed scope value"""
class LayoutViewport(TypedDict, total=True):
    """Layout viewport position and dimensions."""
    pageX: int
    """Horizontal offset relative to the document (CSS pixels)."""
    pageY: int
    """Vertical offset relative to the document (CSS pixels)."""
    clientWidth: int
    """Width (CSS pixels), excludes scrollbar if present."""
    clientHeight: int
    """Height (CSS pixels), excludes scrollbar if present."""
class VisualViewport(TypedDict, total=True):
    """Visual viewport position, dimensions, and scale."""
    offsetX: float
    """Horizontal offset relative to the layout viewport (CSS pixels)."""
    offsetY: float
    """Vertical offset relative to the layout viewport (CSS pixels)."""
    pageX: float
    """Horizontal offset relative to the document (CSS pixels)."""
    pageY: float
    """Vertical offset relative to the document (CSS pixels)."""
    clientWidth: float
    """Width (CSS pixels), excludes scrollbar if present."""
    clientHeight: float
    """Height (CSS pixels), excludes scrollbar if present."""
    scale: float
    """Scale relative to the ideal viewport (size at width=device-width)."""
    zoom: NotRequired[float]
    """Page zoom factor (CSS to device independent pixels ratio)."""
class Viewport(TypedDict, total=True):
    """Viewport for capturing screenshot."""
    x: float
    """X offset in device independent pixels (dip)."""
    y: float
    """Y offset in device independent pixels (dip)."""
    width: float
    """Rectangle width in device independent pixels (dip)."""
    height: float
    """Rectangle height in device independent pixels (dip)."""
    scale: float
    """Page scale factor."""
class FontFamilies(TypedDict, total=False):
    """Generic font families collection."""
    standard: NotRequired[str]
    """The standard font-family."""
    fixed: NotRequired[str]
    """The fixed font-family."""
    serif: NotRequired[str]
    """The serif font-family."""
    sansSerif: NotRequired[str]
    """The sansSerif font-family."""
    cursive: NotRequired[str]
    """The cursive font-family."""
    fantasy: NotRequired[str]
    """The fantasy font-family."""
    math: NotRequired[str]
    """The math font-family."""
class ScriptFontFamilies(TypedDict, total=True):
    """Font families collection for a script."""
    script: str
    """Name of the script which these font families are defined for."""
    fontFamilies: FontFamilies
    """Generic font families collection for the script."""
class FontSizes(TypedDict, total=False):
    """Default font sizes."""
    standard: NotRequired[int]
    """Default standard font size."""
    fixed: NotRequired[int]
    """Default fixed font size."""
ClientNavigationReason = Literal['anchorClick','formSubmissionGet','formSubmissionPost','httpHeaderRefresh','initialFrameNavigation','metaTagRefresh','other','pageBlockInterstitial','reload','scriptInitiated']
ClientNavigationDisposition = Literal['currentTab','newTab','newWindow','download']
class InstallabilityErrorArgument(TypedDict, total=True):
    name: str
    """Argument name (e.g. name:'minimum-icon-size-in-pixels')."""
    value: str
    """Argument value (e.g. value:'64')."""
class InstallabilityError(TypedDict, total=True):
    """The installability error"""
    errorId: str
    """The error id (e.g. 'manifest-missing-suitable-icon')."""
    errorArguments: List[InstallabilityErrorArgument]
    """The list of error arguments (e.g. {name:'minimum-icon-size-in-pixels', value:'64'})."""
ReferrerPolicy = Literal['noReferrer','noReferrerWhenDowngrade','origin','originWhenCrossOrigin','sameOrigin','strictOrigin','strictOriginWhenCrossOrigin','unsafeUrl']
"""The referring-policy used for the navigation."""
class CompilationCacheParams(TypedDict, total=True):
    """Per-script compilation cache parameters for Page.produceCompilationCache"""
    url: str
    """The URL of the script to produce a compilation cache entry for."""
    eager: NotRequired[bool]
    """A hint to the backend whether eager compilation is recommended. (the actual compilation mode used is upon backend discretion)."""
class FileFilter(TypedDict, total=False):
    name: NotRequired[str]
    accepts: NotRequired[List[str]]
class FileHandler(TypedDict, total=True):
    action: str
    name: str
    launchType: str
    """Won't repeat the enums, using string for easy comparison. Same as the other enums below."""
    icons: NotRequired[List[ImageResource]]
    accepts: NotRequired[List[FileFilter]]
    """Mimic a map, name is the key, accepts is the value."""
class ImageResource(TypedDict, total=True):
    """The image definition used in both icon and screenshot."""
    url: str
    """The src field in the definition, but changing to url in favor of consistency."""
    sizes: NotRequired[str]
    type: NotRequired[str]
class LaunchHandler(TypedDict, total=True):
    clientMode: str
class ProtocolHandler(TypedDict, total=True):
    protocol: str
    url: str
class RelatedApplication(TypedDict, total=True):
    url: str
    id: NotRequired[str]
class ScopeExtension(TypedDict, total=True):
    origin: str
    """Instead of using tuple, this field always returns the serialized string for easy understanding and comparison."""
    hasOriginWildcard: bool
class Screenshot(TypedDict, total=True):
    image: ImageResource
    formFactor: str
    label: NotRequired[str]
class ShareTarget(TypedDict, total=True):
    action: str
    method: str
    enctype: str
    title: NotRequired[str]
    """Embed the ShareTargetParams"""
    text: NotRequired[str]
    url: NotRequired[str]
    files: NotRequired[List[FileFilter]]
class Shortcut(TypedDict, total=True):
    name: str
    url: str
class WebAppManifest(TypedDict, total=False):
    backgroundColor: NotRequired[str]
    description: NotRequired[str]
    """The extra description provided by the manifest."""
    dir: NotRequired[str]
    display: NotRequired[str]
    displayOverrides: NotRequired[List[str]]
    """The overrided display mode controlled by the user."""
    fileHandlers: NotRequired[List[FileHandler]]
    """The handlers to open files."""
    icons: NotRequired[List[ImageResource]]
    id: NotRequired[str]
    lang: NotRequired[str]
    launchHandler: NotRequired[LaunchHandler]
    """TODO(crbug.com/1231886): This field is non-standard and part of a Chrome experiment. See: https://github.com/WICG/web-app-launch/blob/main/launch_handler.md"""
    name: NotRequired[str]
    orientation: NotRequired[str]
    preferRelatedApplications: NotRequired[bool]
    protocolHandlers: NotRequired[List[ProtocolHandler]]
    """The handlers to open protocols."""
    relatedApplications: NotRequired[List[RelatedApplication]]
    scope: NotRequired[str]
    scopeExtensions: NotRequired[List[ScopeExtension]]
    """Non-standard, see https://github.com/WICG/manifest-incubations/blob/gh-pages/scope_extensions-explainer.md"""
    screenshots: NotRequired[List[Screenshot]]
    """The screenshots used by chromium."""
    shareTarget: NotRequired[ShareTarget]
    shortName: NotRequired[str]
    shortcuts: NotRequired[List[Shortcut]]
    startUrl: NotRequired[str]
    themeColor: NotRequired[str]
NavigationType = Literal['Navigation','BackForwardCacheRestore']
"""The type of a frameNavigated event."""
BackForwardCacheNotRestoredReason = Literal['NotPrimaryMainFrame','BackForwardCacheDisabled','RelatedActiveContentsExist','HTTPStatusNotOK','SchemeNotHTTPOrHTTPS','Loading','WasGrantedMediaAccess','DisableForRenderFrameHostCalled','DomainNotAllowed','HTTPMethodNotGET','SubframeIsNavigating','Timeout','CacheLimit','JavaScriptExecution','RendererProcessKilled','RendererProcessCrashed','SchedulerTrackedFeatureUsed','ConflictingBrowsingInstance','CacheFlushed','ServiceWorkerVersionActivation','SessionRestored','ServiceWorkerPostMessage','EnteredBackForwardCacheBeforeServiceWorkerHostAdded','RenderFrameHostReused_SameSite','RenderFrameHostReused_CrossSite','ServiceWorkerClaim','IgnoreEventAndEvict','HaveInnerContents','TimeoutPuttingInCache','BackForwardCacheDisabledByLowMemory','BackForwardCacheDisabledByCommandLine','NetworkRequestDatapipeDrainedAsBytesConsumer','NetworkRequestRedirected','NetworkRequestTimeout','NetworkExceedsBufferLimit','NavigationCancelledWhileRestoring','NotMostRecentNavigationEntry','BackForwardCacheDisabledForPrerender','UserAgentOverrideDiffers','ForegroundCacheLimit','ForwardCacheDisabled','BrowsingInstanceNotSwapped','BackForwardCacheDisabledForDelegate','UnloadHandlerExistsInMainFrame','UnloadHandlerExistsInSubFrame','ServiceWorkerUnregistration','CacheControlNoStore','CacheControlNoStoreCookieModified','CacheControlNoStoreHTTPOnlyCookieModified','NoResponseHead','Unknown','ActivationNavigationsDisallowedForBug1234857','ErrorDocument','FencedFramesEmbedder','CookieDisabled','HTTPAuthRequired','CookieFlushed','BroadcastChannelOnMessage','WebViewSettingsChanged','WebViewJavaScriptObjectChanged','WebViewMessageListenerInjected','WebViewSafeBrowsingAllowlistChanged','WebViewDocumentStartJavascriptChanged','WebSocket','WebTransport','WebRTC','MainResourceHasCacheControlNoStore','MainResourceHasCacheControlNoCache','SubresourceHasCacheControlNoStore','SubresourceHasCacheControlNoCache','ContainsPlugins','DocumentLoaded','OutstandingNetworkRequestOthers','RequestedMIDIPermission','RequestedAudioCapturePermission','RequestedVideoCapturePermission','RequestedBackForwardCacheBlockedSensors','RequestedBackgroundWorkPermission','BroadcastChannel','WebXR','SharedWorker','SharedWorkerMessage','SharedWorkerWithNoActiveClient','WebLocks','WebLocksContention','WebHID','WebBluetooth','WebShare','RequestedStorageAccessGrant','WebNfc','OutstandingNetworkRequestFetch','OutstandingNetworkRequestXHR','AppBanner','Printing','WebDatabase','PictureInPicture','SpeechRecognizer','IdleManager','PaymentManager','SpeechSynthesis','KeyboardLock','WebOTPService','OutstandingNetworkRequestDirectSocket','InjectedJavascript','InjectedStyleSheet','KeepaliveRequest','IndexedDBEvent','Dummy','JsNetworkRequestReceivedCacheControlNoStoreResource','WebRTCUsedWithCCNS','WebTransportUsedWithCCNS','WebSocketUsedWithCCNS','SmartCard','LiveMediaStreamTrack','UnloadHandler','ParserAborted','ContentSecurityHandler','ContentWebAuthenticationAPI','ContentFileChooser','ContentSerial','ContentFileSystemAccess','ContentMediaDevicesDispatcherHost','ContentWebBluetooth','ContentWebUSB','ContentMediaSessionService','ContentScreenReader','ContentDiscarded','EmbedderPopupBlockerTabHelper','EmbedderSafeBrowsingTriggeredPopupBlocker','EmbedderSafeBrowsingThreatDetails','EmbedderAppBannerManager','EmbedderDomDistillerViewerSource','EmbedderDomDistillerSelfDeletingRequestDelegate','EmbedderOomInterventionTabHelper','EmbedderOfflinePage','EmbedderChromePasswordManagerClientBindCredentialManager','EmbedderPermissionRequestManager','EmbedderModalDialog','EmbedderExtensions','EmbedderExtensionMessaging','EmbedderExtensionMessagingForOpenPort','EmbedderExtensionSentMessageToCachedFrame','RequestedByWebViewClient','PostMessageByWebViewClient','CacheControlNoStoreDeviceBoundSessionTerminated','CacheLimitPrunedOnModerateMemoryPressure','CacheLimitPrunedOnCriticalMemoryPressure']
"""List of not restored reasons for back-forward cache."""
BackForwardCacheNotRestoredReasonType = Literal['SupportPending','PageSupportNeeded','Circumstantial']
"""Types of not restored reasons for back-forward cache."""
class BackForwardCacheBlockingDetails(TypedDict, total=True):
    lineNumber: int
    """Line number in the script (0-based)."""
    columnNumber: int
    """Column number in the script (0-based)."""
    url: NotRequired[str]
    """Url of the file where blockage happened. Optional because of tests."""
    function: NotRequired[str]
    """Function name where blockage happened. Optional because of anonymous functions and tests."""
class BackForwardCacheNotRestoredExplanation(TypedDict, total=True):
    type: BackForwardCacheNotRestoredReasonType
    """Type of the reason"""
    reason: BackForwardCacheNotRestoredReason
    """Not restored reason"""
    context: NotRequired[str]
    """Context associated with the reason. The meaning of this context is dependent on the reason: - EmbedderExtensionSentMessageToCachedFrame: the extension ID."""
    details: NotRequired[List[BackForwardCacheBlockingDetails]]
class BackForwardCacheNotRestoredExplanationTree(TypedDict, total=True):
    url: str
    """URL of each frame"""
    explanations: List[BackForwardCacheNotRestoredExplanation]
    """Not restored reasons of each frame"""
    children: List[BackForwardCacheNotRestoredExplanationTree]
    """Array of children frame"""