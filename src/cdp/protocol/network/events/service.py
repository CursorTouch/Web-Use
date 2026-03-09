"""CDP Network Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class NetworkEvents:
    """
    Events for the Network domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Network events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_data_received(self, callback: Callable[[dataReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when data chunk was received over the network.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: dataReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.dataReceived', callback)
    def on_event_source_message_received(self, callback: Callable[[eventSourceMessageReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when EventSource message is received.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: eventSourceMessageReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.eventSourceMessageReceived', callback)
    def on_loading_failed(self, callback: Callable[[loadingFailedEvent, str | None], None] | None = None) -> None:
        """
    Fired when HTTP request has failed to load.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: loadingFailedEvent, session_id: str | None).
        """
        self.client.on('Network.loadingFailed', callback)
    def on_loading_finished(self, callback: Callable[[loadingFinishedEvent, str | None], None] | None = None) -> None:
        """
    Fired when HTTP request has finished loading.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: loadingFinishedEvent, session_id: str | None).
        """
        self.client.on('Network.loadingFinished', callback)
    def on_request_served_from_cache(self, callback: Callable[[requestServedFromCacheEvent, str | None], None] | None = None) -> None:
        """
    Fired if request ended up loading from cache.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: requestServedFromCacheEvent, session_id: str | None).
        """
        self.client.on('Network.requestServedFromCache', callback)
    def on_request_will_be_sent(self, callback: Callable[[requestWillBeSentEvent, str | None], None] | None = None) -> None:
        """
    Fired when page is about to send HTTP request.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: requestWillBeSentEvent, session_id: str | None).
        """
        self.client.on('Network.requestWillBeSent', callback)
    def on_resource_changed_priority(self, callback: Callable[[resourceChangedPriorityEvent, str | None], None] | None = None) -> None:
        """
    Fired when resource loading priority is changed    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: resourceChangedPriorityEvent, session_id: str | None).
        """
        self.client.on('Network.resourceChangedPriority', callback)
    def on_signed_exchange_received(self, callback: Callable[[signedExchangeReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when a signed exchange was received over the network    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: signedExchangeReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.signedExchangeReceived', callback)
    def on_response_received(self, callback: Callable[[responseReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when HTTP response is available.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: responseReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.responseReceived', callback)
    def on_web_socket_closed(self, callback: Callable[[webSocketClosedEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket is closed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketClosedEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketClosed', callback)
    def on_web_socket_created(self, callback: Callable[[webSocketCreatedEvent, str | None], None] | None = None) -> None:
        """
    Fired upon WebSocket creation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketCreatedEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketCreated', callback)
    def on_web_socket_frame_error(self, callback: Callable[[webSocketFrameErrorEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket message error occurs.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketFrameErrorEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketFrameError', callback)
    def on_web_socket_frame_received(self, callback: Callable[[webSocketFrameReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket message is received.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketFrameReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketFrameReceived', callback)
    def on_web_socket_frame_sent(self, callback: Callable[[webSocketFrameSentEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket message is sent.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketFrameSentEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketFrameSent', callback)
    def on_web_socket_handshake_response_received(self, callback: Callable[[webSocketHandshakeResponseReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket handshake response becomes available.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketHandshakeResponseReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketHandshakeResponseReceived', callback)
    def on_web_socket_will_send_handshake_request(self, callback: Callable[[webSocketWillSendHandshakeRequestEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebSocket is about to initiate handshake.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webSocketWillSendHandshakeRequestEvent, session_id: str | None).
        """
        self.client.on('Network.webSocketWillSendHandshakeRequest', callback)
    def on_web_transport_created(self, callback: Callable[[webTransportCreatedEvent, str | None], None] | None = None) -> None:
        """
    Fired upon WebTransport creation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webTransportCreatedEvent, session_id: str | None).
        """
        self.client.on('Network.webTransportCreated', callback)
    def on_web_transport_connection_established(self, callback: Callable[[webTransportConnectionEstablishedEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebTransport handshake is finished.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webTransportConnectionEstablishedEvent, session_id: str | None).
        """
        self.client.on('Network.webTransportConnectionEstablished', callback)
    def on_web_transport_closed(self, callback: Callable[[webTransportClosedEvent, str | None], None] | None = None) -> None:
        """
    Fired when WebTransport is disposed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: webTransportClosedEvent, session_id: str | None).
        """
        self.client.on('Network.webTransportClosed', callback)
    def on_direct_tcp_socket_created(self, callback: Callable[[directTCPSocketCreatedEvent, str | None], None] | None = None) -> None:
        """
    Fired upon direct_socket.TCPSocket creation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketCreatedEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketCreated', callback)
    def on_direct_tcp_socket_opened(self, callback: Callable[[directTCPSocketOpenedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.TCPSocket connection is opened.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketOpenedEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketOpened', callback)
    def on_direct_tcp_socket_aborted(self, callback: Callable[[directTCPSocketAbortedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.TCPSocket is aborted.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketAbortedEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketAborted', callback)
    def on_direct_tcp_socket_closed(self, callback: Callable[[directTCPSocketClosedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.TCPSocket is closed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketClosedEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketClosed', callback)
    def on_direct_tcp_socket_chunk_sent(self, callback: Callable[[directTCPSocketChunkSentEvent, str | None], None] | None = None) -> None:
        """
    Fired when data is sent to tcp direct socket stream.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketChunkSentEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketChunkSent', callback)
    def on_direct_tcp_socket_chunk_received(self, callback: Callable[[directTCPSocketChunkReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when data is received from tcp direct socket stream.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directTCPSocketChunkReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.directTCPSocketChunkReceived', callback)
    def on_direct_udp_socket_joined_multicast_group(self, callback: Callable[[directUDPSocketJoinedMulticastGroupEvent, str | None], None] | None = None) -> None:
        """
    No description available for directUDPSocketJoinedMulticastGroup.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketJoinedMulticastGroupEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketJoinedMulticastGroup', callback)
    def on_direct_udp_socket_left_multicast_group(self, callback: Callable[[directUDPSocketLeftMulticastGroupEvent, str | None], None] | None = None) -> None:
        """
    No description available for directUDPSocketLeftMulticastGroup.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketLeftMulticastGroupEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketLeftMulticastGroup', callback)
    def on_direct_udp_socket_created(self, callback: Callable[[directUDPSocketCreatedEvent, str | None], None] | None = None) -> None:
        """
    Fired upon direct_socket.UDPSocket creation.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketCreatedEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketCreated', callback)
    def on_direct_udp_socket_opened(self, callback: Callable[[directUDPSocketOpenedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.UDPSocket connection is opened.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketOpenedEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketOpened', callback)
    def on_direct_udp_socket_aborted(self, callback: Callable[[directUDPSocketAbortedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.UDPSocket is aborted.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketAbortedEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketAborted', callback)
    def on_direct_udp_socket_closed(self, callback: Callable[[directUDPSocketClosedEvent, str | None], None] | None = None) -> None:
        """
    Fired when direct_socket.UDPSocket is closed.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketClosedEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketClosed', callback)
    def on_direct_udp_socket_chunk_sent(self, callback: Callable[[directUDPSocketChunkSentEvent, str | None], None] | None = None) -> None:
        """
    Fired when message is sent to udp direct socket stream.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketChunkSentEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketChunkSent', callback)
    def on_direct_udp_socket_chunk_received(self, callback: Callable[[directUDPSocketChunkReceivedEvent, str | None], None] | None = None) -> None:
        """
    Fired when message is received from udp direct socket stream.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: directUDPSocketChunkReceivedEvent, session_id: str | None).
        """
        self.client.on('Network.directUDPSocketChunkReceived', callback)
    def on_request_will_be_sent_extra_info(self, callback: Callable[[requestWillBeSentExtraInfoEvent, str | None], None] | None = None) -> None:
        """
    Fired when additional information about a requestWillBeSent event is available from the network stack. Not every requestWillBeSent event will have an additional requestWillBeSentExtraInfo fired for it, and there is no guarantee whether requestWillBeSent or requestWillBeSentExtraInfo will be fired first for the same request.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: requestWillBeSentExtraInfoEvent, session_id: str | None).
        """
        self.client.on('Network.requestWillBeSentExtraInfo', callback)
    def on_response_received_extra_info(self, callback: Callable[[responseReceivedExtraInfoEvent, str | None], None] | None = None) -> None:
        """
    Fired when additional information about a responseReceived event is available from the network stack. Not every responseReceived event will have an additional responseReceivedExtraInfo for it, and responseReceivedExtraInfo may be fired before or after responseReceived.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: responseReceivedExtraInfoEvent, session_id: str | None).
        """
        self.client.on('Network.responseReceivedExtraInfo', callback)
    def on_response_received_early_hints(self, callback: Callable[[responseReceivedEarlyHintsEvent, str | None], None] | None = None) -> None:
        """
    Fired when 103 Early Hints headers is received in addition to the common response. Not every responseReceived event will have an responseReceivedEarlyHints fired. Only one responseReceivedEarlyHints may be fired for eached responseReceived event.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: responseReceivedEarlyHintsEvent, session_id: str | None).
        """
        self.client.on('Network.responseReceivedEarlyHints', callback)
    def on_trust_token_operation_done(self, callback: Callable[[trustTokenOperationDoneEvent, str | None], None] | None = None) -> None:
        """
    Fired exactly once for each Trust Token operation. Depending on the type of the operation and whether the operation succeeded or failed, the event is fired before the corresponding request was sent or after the response was received.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: trustTokenOperationDoneEvent, session_id: str | None).
        """
        self.client.on('Network.trustTokenOperationDone', callback)
    def on_policy_updated(self, callback: Callable[[policyUpdatedEvent, str | None], None] | None = None) -> None:
        """
    Fired once security policy has been updated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: policyUpdatedEvent, session_id: str | None).
        """
        self.client.on('Network.policyUpdated', callback)
    def on_reporting_api_report_added(self, callback: Callable[[reportingApiReportAddedEvent, str | None], None] | None = None) -> None:
        """
    Is sent whenever a new report is added. And after 'enableReportingApi' for all existing reports.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: reportingApiReportAddedEvent, session_id: str | None).
        """
        self.client.on('Network.reportingApiReportAdded', callback)
    def on_reporting_api_report_updated(self, callback: Callable[[reportingApiReportUpdatedEvent, str | None], None] | None = None) -> None:
        """
    No description available for reportingApiReportUpdated.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: reportingApiReportUpdatedEvent, session_id: str | None).
        """
        self.client.on('Network.reportingApiReportUpdated', callback)
    def on_reporting_api_endpoints_changed_for_origin(self, callback: Callable[[reportingApiEndpointsChangedForOriginEvent, str | None], None] | None = None) -> None:
        """
    No description available for reportingApiEndpointsChangedForOrigin.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: reportingApiEndpointsChangedForOriginEvent, session_id: str | None).
        """
        self.client.on('Network.reportingApiEndpointsChangedForOrigin', callback)
    def on_device_bound_sessions_added(self, callback: Callable[[deviceBoundSessionsAddedEvent, str | None], None] | None = None) -> None:
        """
    Triggered when the initial set of device bound sessions is added.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: deviceBoundSessionsAddedEvent, session_id: str | None).
        """
        self.client.on('Network.deviceBoundSessionsAdded', callback)
    def on_device_bound_session_event_occurred(self, callback: Callable[[deviceBoundSessionEventOccurredEvent, str | None], None] | None = None) -> None:
        """
    Triggered when a device bound session event occurs.    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: deviceBoundSessionEventOccurredEvent, session_id: str | None).
        """
        self.client.on('Network.deviceBoundSessionEventOccurred', callback)