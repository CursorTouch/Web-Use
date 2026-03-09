from jinja2_strcase import StrcaseExtension
from jinja2 import Environment

DOMAINS_TEMPLATE = """\
\"\"\"CDP Domains library for interacting with various domains.\"\"\"
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .service import Client
    {% for domain in domains %}
    from .protocol.{{ domain['domain'] | to_snake }}.service import {{ domain['domain'] }}
    {% endfor %}

class Domains:
    \"\"\"
    Collection of all CDP domains.
    
    This class acts as a container for all available CDP domain services. 
    Each domain is lazily initialized when first accessed.
    \"\"\"
    def __init__(self, client: "Client"):
        \"\"\"
        Initialize the Domains container.
        
        Args:
            client ("Client"): The parent CDP client instance.
        \"\"\"
        self.client = client
        {% for domain in domains %}
        self._{{ domain['domain'] | to_snake }}: Optional['{{ domain['domain'] }}'] = None
        {% endfor %}

    {% for domain in domains %}
    @property
    def {{ domain['domain'] | to_snake }}(self) -> '{{ domain['domain'] }}':
        \"\"\"
        {% if domain['description'] %}{{ domain['description'] | replace("\\n", " ") }}{% else %}Access the {{ domain['domain'] }} domain.{% endif %}
        \"\"\"
        if self._{{ domain['domain'] | to_snake }} is None:
            from .protocol.{{ domain['domain'] | to_snake }}.service import {{ domain['domain'] }}
            self._{{ domain['domain'] | to_snake }} = {{ domain['domain'] }}(client=self.client)
        return self._{{ domain['domain'] | to_snake }}

    {% endfor %}
"""

SERVICE_TEMPLATE = """\
from typing import Optional, Dict, Any, Callable,Annotated, List
from operator import add
import websockets
import asyncio
import logging
import json

from .domains import Domains
from .generator.service import CDPGenerator

class Client(Domains):
    \"\"\"
    Core client for interacting with Chrome DevTools Protocol (CDP).
    
    This class provides a high-level API to send commands and listen for events across
    various CDP domains. It manages the underlying WebSocket connection and dispatches
    messages to the appropriate handlers.
    
    Attributes:
        url (str): The WebSocket URL of the remote debugging target.
        ws (websockets.ClientConnection): The active WebSocket connection.
        listen_task (asyncio.Task): Background task processing incoming CDP messages.
        id_counter (int): Counter for generating unique request IDs.
        pending_requests (Dict[int, asyncio.Future]): Tracks outstanding requests by ID.
        event_handlers (Dict[str, List[Callable]]): Registered callbacks for CDP events.
    \"\"\"
    def __init__(self, url: str, refresh: bool = False):
        \"\"\"
        Initialize the CDP Client.
        
        Args:
            url (str): WebSocket debugger URL.
            refresh (bool): If True, regenerates the CDP protocol definitions on initialization.
        \"\"\"
        super().__init__(self)
        self.url = url
        self.ws :Optional[websockets.ClientConnection] = None
        self.listen_task :Optional[asyncio.Task] = None
        self.id_counter: Annotated[int, add] = 0
        self.pending_requests: Dict[int, asyncio.Future] = {}
        self.event_handlers: Dict[str, List[Callable[[Any, Optional[str]], None]]] = {}
        
        if refresh:
            self.refresh()

    async def __aenter__(self):
        \"\"\"Connect to the WebSocket and start the background listener.\"\"\"
        self.ws = await websockets.connect(self.url,max_size=100*1024*1024)
        self.listen_task = asyncio.create_task(self.listen())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        \"\"\"Cancel the listener, clear pending requests, and close the WebSocket.\"\"\"
        for future in self.pending_requests.values():
            if not future.done():
                future.set_exception(Exception("WebSocket connection closed"))
        self.pending_requests.clear()
        if self.listen_task:
            try:
                self.listen_task.cancel()
                await self.listen_task
            except asyncio.CancelledError:
                pass
            finally:
                self.listen_task = None
        if self.ws:
            await self.ws.close()
            self.ws = None

    async def send(self, method: str, params: Optional[dict] = None,session_id: Optional[str] = None) -> Any:
        \"\"\"
        Send a CDP command and wait for the result.
        
        Args:
            method (str): The CDP method name (e.g., 'Page.navigate').
            params (dict, optional): Parameters for the method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
            Any: The 'result' object from the CDP response.
            
        Raises:
            Exception: If the CDP returns an error or the connection is lost.
        \"\"\"
        self.id_counter+=1
        future = asyncio.Future()
        self.pending_requests[self.id_counter] = future
        
        try:
            message = {"id": self.id_counter, "method": method, "params": params or {}}
            if session_id:
                message['sessionId'] = session_id
            await self.ws.send(json.dumps(message))
            return await future
        except Exception as e:
            self.pending_requests.pop(self.id_counter, None)
            raise e

    def on(self, event: str, callback: Callable[[Any, Optional[str]], None]) -> None:
        \"\"\"
        Register an event handler. Alias for `Client.register`.
        
        Args:
            event (str): The CDP event name (e.g., 'Page.loadEventFired').
            callback (callable): Function called with (params, session_id).
        \"\"\"
        self.register(event, callback)

    def register(self, event: str, callback: Callable[[Any, Optional[str]], None]) -> None:
        \"\"\"
        Register a handler for a specific CDP event.
        
        Args:
            event (str): The CDP event name.
            callback (callable): Function called with (params, session_id).
        \"\"\"
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(callback)

    def unregister(self, event: str) -> None:
        \"\"\"
        Unregister all handlers for a specific CDP event.
        
        Args:
            event (str): The CDP event name.
        \"\"\"
        if event in self.event_handlers:
            del self.event_handlers[event]
    
    def refresh(self):
        \"\"\"
        Refresh the CDP protocol definitions by fetching latest schemas and 
        regenerating the client source code on disk.
        \"\"\"
        generator = CDPGenerator()
        generator.generate()

    async def listen(self):
        \"\"\"
        Internal background loop that receives messages from the WebSocket.
        Dispatches responses to pending request futures and events to registered handlers.
        \"\"\"
        while True:
            try:
                message = await self.ws.recv()
                data = json.loads(message)
                if "id" in data:
                    # Method
                    request_id=data["id"]
                    logging.debug(f"Received method response: {data}")
                    if request_id not in self.pending_requests:
                        continue
                    future = self.pending_requests.pop(request_id)
                    if not future.done():
                        if "error" in data:
                            future.set_exception(Exception(data.get("error")))
                        else:
                            future.set_result(data.get("result"))
                elif 'method' in data:
                    # Event
                    method=data.get("method")
                    params = data.get("params", {})
                    session_id=data.get("sessionId")
                    logging.debug(f"Received event: {data}")
                    if method not in self.event_handlers:
                        continue
                    
                    handlers = self.event_handlers[method]
                    for handler in handlers:
                        try:
                            if asyncio.iscoroutinefunction(handler):
                                asyncio.create_task(handler(params,session_id))
                            else:
                                handler(params,session_id)
                        except Exception as e:
                            logging.error(f"Error in event handler for {method}: {e}")
                            continue
            except websockets.exceptions.ConnectionClosed:
                logging.info("CDP WebSocket connection closed")
                break
            except Exception as e:
                logging.error(f"Error in CDP listen loop: {e}")
                break
"""

class ClientGenerator:
    def __init__(self, protocol_package: str, package_name: str):
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])
        self.protocol_package = protocol_package
        self.package_name = package_name

    def generate_domains(self, domains: list[dict]):
        template = self.env.from_string(DOMAINS_TEMPLATE)
        return template.render(domains=domains, protocol_package=self.protocol_package).strip()

    def generate_service(self):
        template = self.env.from_string(SERVICE_TEMPLATE)
        return template.render().strip()