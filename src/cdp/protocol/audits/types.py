"""CDP Audits Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.network.types import ClientSecurityState
    from cdp.protocol.network.types import CorsErrorStatus
    from cdp.protocol.network.types import IPAddressSpace
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.network.types import RequestId
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.runtime.types import ScriptId
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.runtime.types import UniqueDebuggerId

class AffectedCookie(TypedDict, total=True):
    """Information about a cookie that is affected by an inspector issue."""
    name: str
    """The following three properties uniquely identify a cookie"""
    path: str
    domain: str
class AffectedRequest(TypedDict, total=True):
    """Information about a request that is affected by an inspector issue."""
    url: str
    requestId: NotRequired[RequestId]
    """The unique request id."""
class AffectedFrame(TypedDict, total=True):
    """Information about the frame affected by an inspector issue."""
    frameId: FrameId
CookieExclusionReason = Literal['ExcludeSameSiteUnspecifiedTreatedAsLax','ExcludeSameSiteNoneInsecure','ExcludeSameSiteLax','ExcludeSameSiteStrict','ExcludeDomainNonASCII','ExcludeThirdPartyCookieBlockedInFirstPartySet','ExcludeThirdPartyPhaseout','ExcludePortMismatch','ExcludeSchemeMismatch']
CookieWarningReason = Literal['WarnSameSiteUnspecifiedCrossSiteContext','WarnSameSiteNoneInsecure','WarnSameSiteUnspecifiedLaxAllowUnsafe','WarnSameSiteStrictLaxDowngradeStrict','WarnSameSiteStrictCrossDowngradeStrict','WarnSameSiteStrictCrossDowngradeLax','WarnSameSiteLaxCrossDowngradeStrict','WarnSameSiteLaxCrossDowngradeLax','WarnAttributeValueExceedsMaxSize','WarnDomainNonASCII','WarnThirdPartyPhaseout','WarnCrossSiteRedirectDowngradeChangesInclusion','WarnDeprecationTrialMetadata','WarnThirdPartyCookieHeuristic']
CookieOperation = Literal['SetCookie','ReadCookie']
InsightType = Literal['GitHubResource','GracePeriod','Heuristics']
"""Represents the category of insight that a cookie issue falls under."""
class CookieIssueInsight(TypedDict, total=True):
    """Information about the suggested solution to a cookie issue."""
    type: InsightType
    tableEntryUrl: NotRequired[str]
    """Link to table entry in third-party cookie migration readiness list."""
class CookieIssueDetails(TypedDict, total=True):
    """This information is currently necessary, as the front-end has a difficult time finding a specific cookie. With this, we can convey specific error information without the cookie."""
    cookieWarningReasons: List[CookieWarningReason]
    cookieExclusionReasons: List[CookieExclusionReason]
    operation: CookieOperation
    """Optionally identifies the site-for-cookies and the cookie url, which may be used by the front-end as additional context."""
    cookie: NotRequired[AffectedCookie]
    """If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line is syntactically or semantically malformed in a way that no valid cookie could be created."""
    rawCookieLine: NotRequired[str]
    siteForCookies: NotRequired[str]
    cookieUrl: NotRequired[str]
    request: NotRequired[AffectedRequest]
    insight: NotRequired[CookieIssueInsight]
    """The recommended solution to the issue."""
PerformanceIssueType = Literal['DocumentCookie']
class PerformanceIssueDetails(TypedDict, total=True):
    """Details for a performance issue."""
    performanceIssueType: PerformanceIssueType
    sourceCodeLocation: NotRequired[SourceCodeLocation]
MixedContentResolutionStatus = Literal['MixedContentBlocked','MixedContentAutomaticallyUpgraded','MixedContentWarning']
MixedContentResourceType = Literal['AttributionSrc','Audio','Beacon','CSPReport','Download','EventSource','Favicon','Font','Form','Frame','Image','Import','JSON','Manifest','Ping','PluginData','PluginResource','Prefetch','Resource','Script','ServiceWorker','SharedWorker','SpeculationRules','Stylesheet','Track','Video','Worker','XMLHttpRequest','XSLT']
class MixedContentIssueDetails(TypedDict, total=True):
    resolutionStatus: MixedContentResolutionStatus
    """The way the mixed content issue is being resolved."""
    insecureURL: str
    """The unsafe http url causing the mixed content issue."""
    mainResourceURL: str
    """The url responsible for the call to an unsafe url."""
    resourceType: NotRequired[MixedContentResourceType]
    """The type of resource causing the mixed content issue (css, js, iframe, form,...). Marked as optional because it is mapped to from blink::mojom::RequestContextType, which will be replaced by network::mojom::RequestDestination"""
    request: NotRequired[AffectedRequest]
    """The mixed content request. Does not always exist (e.g. for unsafe form submission urls)."""
    frame: NotRequired[AffectedFrame]
    """Optional because not every mixed content issue is necessarily linked to a frame."""
BlockedByResponseReason = Literal['CoepFrameResourceNeedsCoepHeader','CoopSandboxedIFrameCannotNavigateToCoopPage','CorpNotSameOrigin','CorpNotSameOriginAfterDefaultedToSameOriginByCoep','CorpNotSameOriginAfterDefaultedToSameOriginByDip','CorpNotSameOriginAfterDefaultedToSameOriginByCoepAndDip','CorpNotSameSite','SRIMessageSignatureMismatch']
"""Enum indicating the reason a response has been blocked. These reasons are refinements of the net error BLOCKED_BY_RESPONSE."""
class BlockedByResponseIssueDetails(TypedDict, total=True):
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE code. Currently only used for COEP/COOP, but may be extended to include some CSP errors in the future."""
    request: AffectedRequest
    reason: BlockedByResponseReason
    parentFrame: NotRequired[AffectedFrame]
    blockedFrame: NotRequired[AffectedFrame]
HeavyAdResolutionStatus = Literal['HeavyAdBlocked','HeavyAdWarning']
HeavyAdReason = Literal['NetworkTotalLimit','CpuTotalLimit','CpuPeakLimit']
class HeavyAdIssueDetails(TypedDict, total=True):
    resolution: HeavyAdResolutionStatus
    """The resolution status, either blocking the content or warning."""
    reason: HeavyAdReason
    """The reason the ad was blocked, total network or cpu or peak cpu."""
    frame: AffectedFrame
    """The frame that was blocked."""
ContentSecurityPolicyViolationType = Literal['kInlineViolation','kEvalViolation','kURLViolation','kSRIViolation','kTrustedTypesSinkViolation','kTrustedTypesPolicyViolation','kWasmEvalViolation']
class SourceCodeLocation(TypedDict, total=True):
    url: str
    lineNumber: int
    columnNumber: int
    scriptId: NotRequired[ScriptId]
class ContentSecurityPolicyIssueDetails(TypedDict, total=True):
    violatedDirective: str
    """Specific directive that is violated, causing the CSP issue."""
    isReportOnly: bool
    contentSecurityPolicyViolationType: ContentSecurityPolicyViolationType
    blockedURL: NotRequired[str]
    """The url not included in allowed sources."""
    frameAncestor: NotRequired[AffectedFrame]
    sourceCodeLocation: NotRequired[SourceCodeLocation]
    violatingNodeId: NotRequired[BackendNodeId]
SharedArrayBufferIssueType = Literal['TransferIssue','CreationIssue']
class SharedArrayBufferIssueDetails(TypedDict, total=True):
    """Details for a issue arising from an SAB being instantiated in, or transferred to a context that is not cross-origin isolated."""
    sourceCodeLocation: SourceCodeLocation
    isWarning: bool
    type: SharedArrayBufferIssueType
class CorsIssueDetails(TypedDict, total=True):
    """Details for a CORS related issue, e.g. a warning or error related to CORS RFC1918 enforcement."""
    corsErrorStatus: CorsErrorStatus
    isWarning: bool
    request: AffectedRequest
    location: NotRequired[SourceCodeLocation]
    initiatorOrigin: NotRequired[str]
    resourceIPAddressSpace: NotRequired[IPAddressSpace]
    clientSecurityState: NotRequired[ClientSecurityState]
AttributionReportingIssueType = Literal['PermissionPolicyDisabled','UntrustworthyReportingOrigin','InsecureContext','InvalidHeader','InvalidRegisterTriggerHeader','SourceAndTriggerHeaders','SourceIgnored','TriggerIgnored','OsSourceIgnored','OsTriggerIgnored','InvalidRegisterOsSourceHeader','InvalidRegisterOsTriggerHeader','WebAndOsHeaders','NoWebOrOsSupport','NavigationRegistrationWithoutTransientUserActivation','InvalidInfoHeader','NoRegisterSourceHeader','NoRegisterTriggerHeader','NoRegisterOsSourceHeader','NoRegisterOsTriggerHeader','NavigationRegistrationUniqueScopeAlreadySet']
SharedDictionaryError = Literal['UseErrorCrossOriginNoCorsRequest','UseErrorDictionaryLoadFailure','UseErrorMatchingDictionaryNotUsed','UseErrorUnexpectedContentDictionaryHeader','WriteErrorCossOriginNoCorsRequest','WriteErrorDisallowedBySettings','WriteErrorExpiredResponse','WriteErrorFeatureDisabled','WriteErrorInsufficientResources','WriteErrorInvalidMatchField','WriteErrorInvalidStructuredHeader','WriteErrorInvalidTTLField','WriteErrorNavigationRequest','WriteErrorNoMatchField','WriteErrorNonIntegerTTLField','WriteErrorNonListMatchDestField','WriteErrorNonSecureContext','WriteErrorNonStringIdField','WriteErrorNonStringInMatchDestList','WriteErrorNonStringMatchField','WriteErrorNonTokenTypeField','WriteErrorRequestAborted','WriteErrorShuttingDown','WriteErrorTooLongIdField','WriteErrorUnsupportedType']
SRIMessageSignatureError = Literal['MissingSignatureHeader','MissingSignatureInputHeader','InvalidSignatureHeader','InvalidSignatureInputHeader','SignatureHeaderValueIsNotByteSequence','SignatureHeaderValueIsParameterized','SignatureHeaderValueIsIncorrectLength','SignatureInputHeaderMissingLabel','SignatureInputHeaderValueNotInnerList','SignatureInputHeaderValueMissingComponents','SignatureInputHeaderInvalidComponentType','SignatureInputHeaderInvalidComponentName','SignatureInputHeaderInvalidHeaderComponentParameter','SignatureInputHeaderInvalidDerivedComponentParameter','SignatureInputHeaderKeyIdLength','SignatureInputHeaderInvalidParameter','SignatureInputHeaderMissingRequiredParameters','ValidationFailedSignatureExpired','ValidationFailedInvalidLength','ValidationFailedSignatureMismatch','ValidationFailedIntegrityMismatch']
UnencodedDigestError = Literal['MalformedDictionary','UnknownAlgorithm','IncorrectDigestType','IncorrectDigestLength']
ConnectionAllowlistError = Literal['InvalidHeader','MoreThanOneList','ItemNotInnerList','InvalidAllowlistItemType','ReportingEndpointNotToken','InvalidUrlPattern']
class AttributionReportingIssueDetails(TypedDict, total=True):
    """Details for issues around "Attribution Reporting API" usage. Explainer: https://github.com/WICG/attribution-reporting-api"""
    violationType: AttributionReportingIssueType
    request: NotRequired[AffectedRequest]
    violatingNodeId: NotRequired[BackendNodeId]
    invalidParameter: NotRequired[str]
class QuirksModeIssueDetails(TypedDict, total=True):
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode that affects page layouting."""
    isLimitedQuirksMode: bool
    """If false, it means the document's mode is quirks instead of limited-quirks."""
    documentNodeId: BackendNodeId
    url: str
    frameId: FrameId
    loaderId: LoaderId
class NavigatorUserAgentIssueDetails(TypedDict, total=True):
    url: str
    location: NotRequired[SourceCodeLocation]
class SharedDictionaryIssueDetails(TypedDict, total=True):
    sharedDictionaryError: SharedDictionaryError
    request: AffectedRequest
class SRIMessageSignatureIssueDetails(TypedDict, total=True):
    error: SRIMessageSignatureError
    signatureBase: str
    integrityAssertions: List[str]
    request: AffectedRequest
class UnencodedDigestIssueDetails(TypedDict, total=True):
    error: UnencodedDigestError
    request: AffectedRequest
class ConnectionAllowlistIssueDetails(TypedDict, total=True):
    error: ConnectionAllowlistError
    request: AffectedRequest
GenericIssueErrorType = Literal['FormLabelForNameError','FormDuplicateIdForInputError','FormInputWithNoLabelError','FormAutocompleteAttributeEmptyError','FormEmptyIdAndNameAttributesForInputError','FormAriaLabelledByToNonExistingIdError','FormInputAssignedAutocompleteValueToIdOrNameAttributeError','FormLabelHasNeitherForNorNestedInputError','FormLabelForMatchesNonExistingIdError','FormInputHasWrongButWellIntendedAutocompleteValueError','ResponseWasBlockedByORB','NavigationEntryMarkedSkippable','AutofillAndManualTextPolicyControlledFeaturesInfo','AutofillPolicyControlledFeatureInfo','ManualTextPolicyControlledFeatureInfo','FormModelContextParameterMissingTitleAndDescription']
class GenericIssueDetails(TypedDict, total=True):
    """Depending on the concrete errorType, different properties are set."""
    errorType: GenericIssueErrorType
    """Issues with the same errorType are aggregated in the frontend."""
    frameId: NotRequired[FrameId]
    violatingNodeId: NotRequired[BackendNodeId]
    violatingNodeAttribute: NotRequired[str]
    request: NotRequired[AffectedRequest]
class DeprecationIssueDetails(TypedDict, total=True):
    """This issue tracks information needed to print a deprecation message. https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md"""
    sourceCodeLocation: SourceCodeLocation
    type: str
    """One of the deprecation names from third_party/blink/renderer/core/frame/deprecation/deprecation.json5"""
    affectedFrame: NotRequired[AffectedFrame]
class BounceTrackingIssueDetails(TypedDict, total=True):
    """This issue warns about sites in the redirect chain of a finished navigation that may be flagged as trackers and have their state cleared if they don't receive a user interaction. Note that in this context 'site' means eTLD+1. For example, if the URL https://example.test:80/bounce was in the redirect chain, the site reported would be example.test."""
    trackingSites: List[str]
class CookieDeprecationMetadataIssueDetails(TypedDict, total=True):
    """This issue warns about third-party sites that are accessing cookies on the current page, and have been permitted due to having a global metadata grant. Note that in this context 'site' means eTLD+1. For example, if the URL https://example.test:80/web_page was accessing cookies, the site reported would be example.test."""
    allowedSites: List[str]
    optOutPercentage: float
    isOptOutTopLevel: bool
    operation: CookieOperation
ClientHintIssueReason = Literal['MetaTagAllowListInvalidOrigin','MetaTagModifiedHTML']
class FederatedAuthRequestIssueDetails(TypedDict, total=True):
    federatedAuthRequestIssueReason: FederatedAuthRequestIssueReason
FederatedAuthRequestIssueReason = Literal['ShouldEmbargo','TooManyRequests','WellKnownHttpNotFound','WellKnownNoResponse','WellKnownInvalidResponse','WellKnownListEmpty','WellKnownInvalidContentType','ConfigNotInWellKnown','WellKnownTooBig','ConfigHttpNotFound','ConfigNoResponse','ConfigInvalidResponse','ConfigInvalidContentType','IdpNotPotentiallyTrustworthy','DisabledInSettings','DisabledInFlags','ErrorFetchingSignin','InvalidSigninResponse','AccountsHttpNotFound','AccountsNoResponse','AccountsInvalidResponse','AccountsListEmpty','AccountsInvalidContentType','IdTokenHttpNotFound','IdTokenNoResponse','IdTokenInvalidResponse','IdTokenIdpErrorResponse','IdTokenCrossSiteIdpErrorResponse','IdTokenInvalidRequest','IdTokenInvalidContentType','ErrorIdToken','Canceled','RpPageNotVisible','SilentMediationFailure','NotSignedInWithIdp','MissingTransientUserActivation','ReplacedByActiveMode','RelyingPartyOriginIsOpaque','TypeNotMatching','UiDismissedNoEmbargo','CorsError','SuppressedBySegmentationPlatform']
"""Represents the failure reason when a federated authentication reason fails. Should be updated alongside RequestIdTokenStatus in third_party/blink/public/mojom/devtools/inspector_issue.mojom to include all cases except for success."""
class FederatedAuthUserInfoRequestIssueDetails(TypedDict, total=True):
    federatedAuthUserInfoRequestIssueReason: FederatedAuthUserInfoRequestIssueReason
FederatedAuthUserInfoRequestIssueReason = Literal['NotSameOrigin','NotIframe','NotPotentiallyTrustworthy','NoApiPermission','NotSignedInWithIdp','NoAccountSharingPermission','InvalidConfigOrWellKnown','InvalidAccountsResponse','NoReturningUserFromFetchedAccounts']
"""Represents the failure reason when a getUserInfo() call fails. Should be updated alongside FederatedAuthUserInfoRequestResult in third_party/blink/public/mojom/devtools/inspector_issue.mojom."""
class ClientHintIssueDetails(TypedDict, total=True):
    """This issue tracks client hints related issues. It's used to deprecate old features, encourage the use of new ones, and provide general guidance."""
    sourceCodeLocation: SourceCodeLocation
    clientHintIssueReason: ClientHintIssueReason
class FailedRequestInfo(TypedDict, total=True):
    url: str
    """The URL that failed to load."""
    failureMessage: str
    """The failure message for the failed request."""
    requestId: NotRequired[RequestId]
PartitioningBlobURLInfo = Literal['BlockedCrossPartitionFetching','EnforceNoopenerForNavigation']
class PartitioningBlobURLIssueDetails(TypedDict, total=True):
    url: str
    """The BlobURL that failed to load."""
    partitioningBlobURLInfo: PartitioningBlobURLInfo
    """Additional information about the Partitioning Blob URL issue."""
ElementAccessibilityIssueReason = Literal['DisallowedSelectChild','DisallowedOptGroupChild','NonPhrasingContentOptionChild','InteractiveContentOptionChild','InteractiveContentLegendChild','InteractiveContentSummaryDescendant']
class ElementAccessibilityIssueDetails(TypedDict, total=True):
    """This issue warns about errors in the select or summary element content model."""
    nodeId: BackendNodeId
    elementAccessibilityIssueReason: ElementAccessibilityIssueReason
    hasDisallowedAttributes: bool
StyleSheetLoadingIssueReason = Literal['LateImportRule','RequestFailed']
class StylesheetLoadingIssueDetails(TypedDict, total=True):
    """This issue warns when a referenced stylesheet couldn't be loaded."""
    sourceCodeLocation: SourceCodeLocation
    """Source code position that referenced the failing stylesheet."""
    styleSheetLoadingIssueReason: StyleSheetLoadingIssueReason
    """Reason why the stylesheet couldn't be loaded."""
    failedRequestInfo: NotRequired[FailedRequestInfo]
    """Contains additional info when the failure was due to a request."""
PropertyRuleIssueReason = Literal['InvalidSyntax','InvalidInitialValue','InvalidInherits','InvalidName']
class PropertyRuleIssueDetails(TypedDict, total=True):
    """This issue warns about errors in property rules that lead to property registrations being ignored."""
    sourceCodeLocation: SourceCodeLocation
    """Source code position of the property rule."""
    propertyRuleIssueReason: PropertyRuleIssueReason
    """Reason why the property rule was discarded."""
    propertyValue: NotRequired[str]
    """The value of the property rule property that failed to parse"""
UserReidentificationIssueType = Literal['BlockedFrameNavigation','BlockedSubresource','NoisedCanvasReadback']
class UserReidentificationIssueDetails(TypedDict, total=True):
    """This issue warns about uses of APIs that may be considered misuse to re-identify users."""
    type: UserReidentificationIssueType
    request: NotRequired[AffectedRequest]
    """Applies to BlockedFrameNavigation and BlockedSubresource issue types."""
    sourceCodeLocation: NotRequired[SourceCodeLocation]
    """Applies to NoisedCanvasReadback issue type."""
PermissionElementIssueType = Literal['InvalidType','FencedFrameDisallowed','CspFrameAncestorsMissing','PermissionsPolicyBlocked','PaddingRightUnsupported','PaddingBottomUnsupported','InsetBoxShadowUnsupported','RequestInProgress','UntrustedEvent','RegistrationFailed','TypeNotSupported','InvalidTypeActivation','SecurityChecksFailed','ActivationDisabled','GeolocationDeprecated','InvalidDisplayStyle','NonOpaqueColor','LowContrast','FontSizeTooSmall','FontSizeTooLarge','InvalidSizeValue']
class PermissionElementIssueDetails(TypedDict, total=True):
    """This issue warns about improper usage of the <permission> element."""
    issueType: PermissionElementIssueType
    type: NotRequired[str]
    """The value of the type attribute."""
    nodeId: NotRequired[BackendNodeId]
    """The node ID of the <permission> element."""
    isWarning: NotRequired[bool]
    """True if the issue is a warning, false if it is an error."""
    permissionName: NotRequired[str]
    """Fields for message construction: Used for messages that reference a specific permission name"""
    occluderNodeInfo: NotRequired[str]
    """Used for messages about occlusion"""
    occluderParentNodeInfo: NotRequired[str]
    """Used for messages about occluder's parent"""
    disableReason: NotRequired[str]
    """Used for messages about activation disabled reason"""
class AdScriptIdentifier(TypedDict, total=True):
    """Metadata about the ad script that was on the stack that caused the current script in the AdAncestry to be considered ad related."""
    scriptId: ScriptId
    """The script's v8 identifier."""
    debuggerId: UniqueDebuggerId
    """v8's debugging id for the v8::Context."""
    name: str
    """The script's url (or generated name based on id if inline script)."""
class AdAncestry(TypedDict, total=True):
    """Providence about how an ad script was determined to be such. It is an ad because its url matched a filterlist rule, or because some other ad script was on the stack when this script was loaded."""
    adAncestryChain: List[AdScriptIdentifier]
    """The ad-script in the stack when the offending script was loaded. This is recursive down to the root script that was tagged due to the filterlist rule."""
    rootScriptFilterlistRule: NotRequired[str]
    """The filterlist rule that caused the root (last) script in adAncestry to be ad-tagged."""
class SelectivePermissionsInterventionIssueDetails(TypedDict, total=True):
    """The issue warns about blocked calls to privacy sensitive APIs via the Selective Permissions Intervention."""
    apiName: str
    """Which API was intervened on."""
    adAncestry: AdAncestry
    """Why the ad script using the API is considered an ad."""
    stackTrace: NotRequired[StackTrace]
    """The stack trace at the time of the intervention."""
InspectorIssueCode = Literal['CookieIssue','MixedContentIssue','BlockedByResponseIssue','HeavyAdIssue','ContentSecurityPolicyIssue','SharedArrayBufferIssue','CorsIssue','AttributionReportingIssue','QuirksModeIssue','PartitioningBlobURLIssue','NavigatorUserAgentIssue','GenericIssue','DeprecationIssue','ClientHintIssue','FederatedAuthRequestIssue','BounceTrackingIssue','CookieDeprecationMetadataIssue','StylesheetLoadingIssue','FederatedAuthUserInfoRequestIssue','PropertyRuleIssue','SharedDictionaryIssue','ElementAccessibilityIssue','SRIMessageSignatureIssue','UnencodedDigestIssue','ConnectionAllowlistIssue','UserReidentificationIssue','PermissionElementIssue','PerformanceIssue','SelectivePermissionsInterventionIssue']
"""A unique identifier for the type of issue. Each type may use one of the optional fields in InspectorIssueDetails to convey more specific information about the kind of issue."""
class InspectorIssueDetails(TypedDict, total=False):
    """This struct holds a list of optional fields with additional information specific to the kind of issue. When adding a new issue code, please also add a new optional field to this type."""
    cookieIssueDetails: NotRequired[CookieIssueDetails]
    mixedContentIssueDetails: NotRequired[MixedContentIssueDetails]
    blockedByResponseIssueDetails: NotRequired[BlockedByResponseIssueDetails]
    heavyAdIssueDetails: NotRequired[HeavyAdIssueDetails]
    contentSecurityPolicyIssueDetails: NotRequired[ContentSecurityPolicyIssueDetails]
    sharedArrayBufferIssueDetails: NotRequired[SharedArrayBufferIssueDetails]
    corsIssueDetails: NotRequired[CorsIssueDetails]
    attributionReportingIssueDetails: NotRequired[AttributionReportingIssueDetails]
    quirksModeIssueDetails: NotRequired[QuirksModeIssueDetails]
    partitioningBlobURLIssueDetails: NotRequired[PartitioningBlobURLIssueDetails]
    genericIssueDetails: NotRequired[GenericIssueDetails]
    deprecationIssueDetails: NotRequired[DeprecationIssueDetails]
    clientHintIssueDetails: NotRequired[ClientHintIssueDetails]
    federatedAuthRequestIssueDetails: NotRequired[FederatedAuthRequestIssueDetails]
    bounceTrackingIssueDetails: NotRequired[BounceTrackingIssueDetails]
    cookieDeprecationMetadataIssueDetails: NotRequired[CookieDeprecationMetadataIssueDetails]
    stylesheetLoadingIssueDetails: NotRequired[StylesheetLoadingIssueDetails]
    propertyRuleIssueDetails: NotRequired[PropertyRuleIssueDetails]
    federatedAuthUserInfoRequestIssueDetails: NotRequired[FederatedAuthUserInfoRequestIssueDetails]
    sharedDictionaryIssueDetails: NotRequired[SharedDictionaryIssueDetails]
    elementAccessibilityIssueDetails: NotRequired[ElementAccessibilityIssueDetails]
    sriMessageSignatureIssueDetails: NotRequired[SRIMessageSignatureIssueDetails]
    unencodedDigestIssueDetails: NotRequired[UnencodedDigestIssueDetails]
    connectionAllowlistIssueDetails: NotRequired[ConnectionAllowlistIssueDetails]
    userReidentificationIssueDetails: NotRequired[UserReidentificationIssueDetails]
    permissionElementIssueDetails: NotRequired[PermissionElementIssueDetails]
    performanceIssueDetails: NotRequired[PerformanceIssueDetails]
    selectivePermissionsInterventionIssueDetails: NotRequired[SelectivePermissionsInterventionIssueDetails]
IssueId = str
"""A unique id for a DevTools inspector issue. Allows other entities (e.g. exceptions, CDP message, console messages, etc.) to reference an issue."""
class InspectorIssue(TypedDict, total=True):
    """An inspector issue reported from the back-end."""
    code: InspectorIssueCode
    details: InspectorIssueDetails
    issueId: NotRequired[IssueId]
    """A unique id for this issue. May be omitted if no other entity (e.g. exception, CDP message, etc.) is referencing this issue."""