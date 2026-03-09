"""CDP WebAuthn Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.web_authn.types import AuthenticatorId
    from cdp.protocol.web_authn.types import Credential
    from cdp.protocol.web_authn.types import VirtualAuthenticatorOptions

class enableParameters(TypedDict, total=False):
    enableUI: NotRequired[bool]
    """Whether to enable the WebAuthn user interface. Enabling the UI is recommended for debugging and demo purposes, as it is closer to the real experience. Disabling the UI is recommended for automated testing. Supported at the embedder's discretion if UI is available. Defaults to false."""

class addVirtualAuthenticatorParameters(TypedDict, total=True):
    options: VirtualAuthenticatorOptions
class setResponseOverrideBitsParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    isBogusSignature: NotRequired[bool]
    """If isBogusSignature is set, overrides the signature in the authenticator response to be zero. Defaults to false."""
    isBadUV: NotRequired[bool]
    """If isBadUV is set, overrides the UV bit in the flags in the authenticator response to be zero. Defaults to false."""
    isBadUP: NotRequired[bool]
    """If isBadUP is set, overrides the UP bit in the flags in the authenticator response to be zero. Defaults to false."""
class removeVirtualAuthenticatorParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
class addCredentialParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credential: Credential
class getCredentialParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credentialId: str
class getCredentialsParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
class removeCredentialParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credentialId: str
class clearCredentialsParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
class setUserVerifiedParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    isUserVerified: bool
class setAutomaticPresenceSimulationParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    enabled: bool
class setCredentialPropertiesParameters(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credentialId: str
    backupEligibility: NotRequired[bool]
    backupState: NotRequired[bool]


class addVirtualAuthenticatorReturns(TypedDict):
    authenticatorId: AuthenticatorId



class getCredentialReturns(TypedDict):
    credential: Credential
class getCredentialsReturns(TypedDict):
    credentials: List[Credential]