"""CDP Autofill Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.autofill.types import Address
    from cdp.protocol.autofill.types import CreditCard
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.page.types import FrameId

class triggerParameters(TypedDict, total=True):
    fieldId: BackendNodeId
    """Identifies a field that serves as an anchor for autofill."""
    frameId: NotRequired[FrameId]
    """Identifies the frame that field belongs to."""
    card: NotRequired[CreditCard]
    """Credit card information to fill out the form. Credit card data is not saved.  Mutually exclusive with address."""
    address: NotRequired[Address]
    """Address to fill out the form. Address data is not saved. Mutually exclusive with card."""
class setAddressesParameters(TypedDict, total=True):
    addresses: List[Address]