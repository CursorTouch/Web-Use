"""CDP WebAuthn Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.web_authn.types import AuthenticatorId
    from cdp.protocol.web_authn.types import Credential

class credentialAddedEvent(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credential: Credential
class credentialDeletedEvent(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credentialId: str
class credentialUpdatedEvent(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credential: Credential
class credentialAssertedEvent(TypedDict, total=True):
    authenticatorId: AuthenticatorId
    credential: Credential