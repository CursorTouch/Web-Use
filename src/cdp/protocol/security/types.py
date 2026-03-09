"""CDP Security Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import TimeSinceEpoch

CertificateId = int
"""An internal certificate ID value."""
MixedContentType = Literal['blockable','optionally-blockable','none']
"""A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories"""
SecurityState = Literal['unknown','neutral','insecure','secure','info','insecure-broken']
"""The security level of a page or resource."""
class CertificateSecurityState(TypedDict, total=True):
    """Details about the security state of the page certificate."""
    protocol: str
    """Protocol name (e.g. TLS 1.2 or QUIC)."""
    keyExchange: str
    """Key Exchange used by the connection, or the empty string if not applicable."""
    cipher: str
    """Cipher name."""
    certificate: List[str]
    """Page certificate."""
    subjectName: str
    """Certificate subject name."""
    issuer: str
    """Name of the issuing CA."""
    validFrom: TimeSinceEpoch
    """Certificate valid from date."""
    validTo: TimeSinceEpoch
    """Certificate valid to (expiration) date"""
    certificateHasWeakSignature: bool
    """True if the certificate uses a weak signature algorithm."""
    certificateHasSha1Signature: bool
    """True if the certificate has a SHA1 signature in the chain."""
    modernSSL: bool
    """True if modern SSL"""
    obsoleteSslProtocol: bool
    """True if the connection is using an obsolete SSL protocol."""
    obsoleteSslKeyExchange: bool
    """True if the connection is using an obsolete SSL key exchange."""
    obsoleteSslCipher: bool
    """True if the connection is using an obsolete SSL cipher."""
    obsoleteSslSignature: bool
    """True if the connection is using an obsolete SSL signature."""
    keyExchangeGroup: NotRequired[str]
    """(EC)DH group used by the connection, if applicable."""
    mac: NotRequired[str]
    """TLS MAC. Note that AEAD ciphers do not have separate MACs."""
    certificateNetworkError: NotRequired[str]
    """The highest priority network error code, if the certificate has an error."""
SafetyTipStatus = Literal['badReputation','lookalike']
class SafetyTipInfo(TypedDict, total=True):
    safetyTipStatus: SafetyTipStatus
    """Describes whether the page triggers any safety tips or reputation warnings. Default is unknown."""
    safeUrl: NotRequired[str]
    """The URL the safety tip suggested ("Did you mean?"). Only filled in for lookalike matches."""
class VisibleSecurityState(TypedDict, total=True):
    """Security state information about the page."""
    securityState: SecurityState
    """The security level of the page."""
    securityStateIssueIds: List[str]
    """Array of security state issues ids."""
    certificateSecurityState: NotRequired[CertificateSecurityState]
    """Security state details about the page certificate."""
    safetyTipInfo: NotRequired[SafetyTipInfo]
    """The type of Safety Tip triggered on the page. Note that this field will be set even if the Safety Tip UI was not actually shown."""
class SecurityStateExplanation(TypedDict, total=True):
    """An explanation of an factor contributing to the security state."""
    securityState: SecurityState
    """Security state representing the severity of the factor being explained."""
    title: str
    """Title describing the type of factor."""
    summary: str
    """Short phrase describing the type of factor."""
    description: str
    """Full text explanation of the factor."""
    mixedContentType: MixedContentType
    """The type of mixed content described by the explanation."""
    certificate: List[str]
    """Page certificate."""
    recommendations: NotRequired[List[str]]
    """Recommendations to fix any issues."""
class InsecureContentStatus(TypedDict, total=True):
    """Information about insecure content on the page."""
    ranMixedContent: bool
    """Always false."""
    displayedMixedContent: bool
    """Always false."""
    containedMixedForm: bool
    """Always false."""
    ranContentWithCertErrors: bool
    """Always false."""
    displayedContentWithCertErrors: bool
    """Always false."""
    ranInsecureContentStyle: SecurityState
    """Always set to unknown."""
    displayedInsecureContentStyle: SecurityState
    """Always set to unknown."""
CertificateErrorAction = Literal['continue','cancel']
"""The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request."""