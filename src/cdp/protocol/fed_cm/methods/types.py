"""CDP FedCm Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.fed_cm.types import AccountUrlType
    from cdp.protocol.fed_cm.types import DialogButton

class enableParameters(TypedDict, total=False):
    disableRejectionDelay: NotRequired[bool]
    """Allows callers to disable the promise rejection delay that would normally happen, if this is unimportant to what's being tested. (step 4 of https://fedidcg.github.io/FedCM/#browser-api-rp-sign-in)"""

class selectAccountParameters(TypedDict, total=True):
    dialogId: str
    accountIndex: int
class clickDialogButtonParameters(TypedDict, total=True):
    dialogId: str
    dialogButton: DialogButton
class openUrlParameters(TypedDict, total=True):
    dialogId: str
    accountIndex: int
    accountUrlType: AccountUrlType
class dismissDialogParameters(TypedDict, total=True):
    dialogId: str
    triggerCooldown: NotRequired[bool]