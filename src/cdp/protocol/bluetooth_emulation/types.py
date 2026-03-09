"""CDP BluetoothEmulation Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

CentralState = Literal['absent','powered-off','powered-on']
"""Indicates the various states of Central."""
GATTOperationType = Literal['connection','discovery']
"""Indicates the various types of GATT event."""
CharacteristicWriteType = Literal['write-default-deprecated','write-with-response','write-without-response']
"""Indicates the various types of characteristic write."""
CharacteristicOperationType = Literal['read','write','subscribe-to-notifications','unsubscribe-from-notifications']
"""Indicates the various types of characteristic operation."""
DescriptorOperationType = Literal['read','write']
"""Indicates the various types of descriptor operation."""
class ManufacturerData(TypedDict, total=True):
    """Stores the manufacturer data"""
    key: int
    """Company identifier https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml https://usb.org/developers"""
    data: str
    """Manufacturer-specific data (Encoded as a base64 string when passed over JSON)"""
class ScanRecord(TypedDict, total=False):
    """Stores the byte data of the advertisement packet sent by a Bluetooth device."""
    name: NotRequired[str]
    uuids: NotRequired[List[str]]
    appearance: NotRequired[int]
    """Stores the external appearance description of the device."""
    txPower: NotRequired[int]
    """Stores the transmission power of a broadcasting device."""
    manufacturerData: NotRequired[List[ManufacturerData]]
    """Key is the company identifier and the value is an array of bytes of manufacturer specific data."""
class ScanEntry(TypedDict, total=True):
    """Stores the advertisement packet information that is sent by a Bluetooth device."""
    deviceAddress: str
    rssi: int
    scanRecord: ScanRecord
class CharacteristicProperties(TypedDict, total=False):
    """Describes the properties of a characteristic. This follows Bluetooth Core Specification BT 4.2 Vol 3 Part G 3.3.1. Characteristic Properties."""
    broadcast: NotRequired[bool]
    read: NotRequired[bool]
    writeWithoutResponse: NotRequired[bool]
    write: NotRequired[bool]
    notify: NotRequired[bool]
    indicate: NotRequired[bool]
    authenticatedSignedWrites: NotRequired[bool]
    extendedProperties: NotRequired[bool]