"""CDP BluetoothEmulation Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class BluetoothEmulationEvents:
    """
    Events for the BluetoothEmulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the BluetoothEmulation events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_gatt_operation_received(self, callback: Callable[[gattOperationReceivedEvent, str | None], None] | None = None) -> None:
        """
    Event for when a GATT operation of |type| to the peripheral with |address| happened.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: gattOperationReceivedEvent, session_id: str | None).
        """
        self.client.on('BluetoothEmulation.gattOperationReceived', callback)
    def on_characteristic_operation_received(self, callback: Callable[[characteristicOperationReceivedEvent, str | None], None] | None = None) -> None:
        """
    Event for when a characteristic operation of |type| to the characteristic respresented by |characteristicId| happened. |data| and |writeType| is expected to exist when |type| is write.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: characteristicOperationReceivedEvent, session_id: str | None).
        """
        self.client.on('BluetoothEmulation.characteristicOperationReceived', callback)
    def on_descriptor_operation_received(self, callback: Callable[[descriptorOperationReceivedEvent, str | None], None] | None = None) -> None:
        """
    Event for when a descriptor operation of |type| to the descriptor respresented by |descriptorId| happened. |data| is expected to exist when |type| is write.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: descriptorOperationReceivedEvent, session_id: str | None).
        """
        self.client.on('BluetoothEmulation.descriptorOperationReceived', callback)