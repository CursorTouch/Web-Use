"""CDP Autofill Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.dom.types import BackendNodeId
    from cdp.protocol.page.types import FrameId

class CreditCard(TypedDict, total=True):
    number: str
    """16-digit credit card number."""
    name: str
    """Name of the credit card owner."""
    expiryMonth: str
    """2-digit expiry month."""
    expiryYear: str
    """4-digit expiry year."""
    cvc: str
    """3-digit card verification code."""
class AddressField(TypedDict, total=True):
    name: str
    """address field name, for example GIVEN_NAME. The full list of supported field names: https://source.chromium.org/chromium/chromium/src/+/main:components/autofill/core/browser/field_types.cc;l=38"""
    value: str
    """address field value, for example Jon Doe."""
class AddressFields(TypedDict, total=True):
    """A list of address fields."""
    fields: List[AddressField]
class Address(TypedDict, total=True):
    fields: List[AddressField]
    """fields and values defining an address."""
class AddressUI(TypedDict, total=True):
    """Defines how an address can be displayed like in chrome://settings/addresses. Address UI is a two dimensional array, each inner array is an "address information line", and when rendered in a UI surface should be displayed as such. The following address UI for instance: [[{name: "GIVE_NAME", value: "Jon"}, {name: "FAMILY_NAME", value: "Doe"}], [{name: "CITY", value: "Munich"}, {name: "ZIP", value: "81456"}]] should allow the receiver to render: Jon Doe Munich 81456"""
    addressFields: List[AddressFields]
    """A two dimension array containing the representation of values from an address profile."""
FillingStrategy = Literal['autocompleteAttribute','autofillInferred']
"""Specified whether a filled field was done so by using the html autocomplete attribute or autofill heuristics."""
class FilledField(TypedDict, total=True):
    htmlType: str
    """The type of the field, e.g text, password etc."""
    id: str
    """the html id"""
    name: str
    """the html name"""
    value: str
    """the field value"""
    autofillType: str
    """The actual field type, e.g FAMILY_NAME"""
    fillingStrategy: FillingStrategy
    """The filling strategy"""
    frameId: FrameId
    """The frame the field belongs to"""
    fieldId: BackendNodeId
    """The form field's DOM node"""