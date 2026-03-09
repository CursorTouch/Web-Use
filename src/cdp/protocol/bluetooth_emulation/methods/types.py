"""CDP BluetoothEmulation Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.bluetooth_emulation.types import CentralState
    from cdp.protocol.bluetooth_emulation.types import CharacteristicOperationType
    from cdp.protocol.bluetooth_emulation.types import CharacteristicProperties
    from cdp.protocol.bluetooth_emulation.types import DescriptorOperationType
    from cdp.protocol.bluetooth_emulation.types import GATTOperationType
    from cdp.protocol.bluetooth_emulation.types import ManufacturerData
    from cdp.protocol.bluetooth_emulation.types import ScanEntry

class enableParameters(TypedDict, total=True):
    state: CentralState
    """State of the simulated central."""
    leSupported: bool
    """If the simulated central supports low-energy."""
class setSimulatedCentralStateParameters(TypedDict, total=True):
    state: CentralState
    """State of the simulated central."""

class simulatePreconnectedPeripheralParameters(TypedDict, total=True):
    address: str
    name: str
    manufacturerData: List[ManufacturerData]
    knownServiceUuids: List[str]
class simulateAdvertisementParameters(TypedDict, total=True):
    entry: ScanEntry
class simulateGATTOperationResponseParameters(TypedDict, total=True):
    address: str
    type: GATTOperationType
    code: int
class simulateCharacteristicOperationResponseParameters(TypedDict, total=True):
    characteristicId: str
    type: CharacteristicOperationType
    code: int
    data: NotRequired[str]
class simulateDescriptorOperationResponseParameters(TypedDict, total=True):
    descriptorId: str
    type: DescriptorOperationType
    code: int
    data: NotRequired[str]
class addServiceParameters(TypedDict, total=True):
    address: str
    serviceUuid: str
class removeServiceParameters(TypedDict, total=True):
    serviceId: str
class addCharacteristicParameters(TypedDict, total=True):
    serviceId: str
    characteristicUuid: str
    properties: CharacteristicProperties
class removeCharacteristicParameters(TypedDict, total=True):
    characteristicId: str
class addDescriptorParameters(TypedDict, total=True):
    characteristicId: str
    descriptorUuid: str
class removeDescriptorParameters(TypedDict, total=True):
    descriptorId: str
class simulateGATTDisconnectionParameters(TypedDict, total=True):
    address: str








class addServiceReturns(TypedDict):
    serviceId: str
    """An identifier that uniquely represents this service."""

class addCharacteristicReturns(TypedDict):
    characteristicId: str
    """An identifier that uniquely represents this characteristic."""

class addDescriptorReturns(TypedDict):
    descriptorId: str
    """An identifier that uniquely represents this descriptor."""