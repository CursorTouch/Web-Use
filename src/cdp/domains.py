"""CDP Domains library for interacting with various domains."""
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from .service import Client
    from .protocol.accessibility.service import Accessibility
    from .protocol.animation.service import Animation
    from .protocol.audits.service import Audits
    from .protocol.autofill.service import Autofill
    from .protocol.background_service.service import BackgroundService
    from .protocol.bluetooth_emulation.service import BluetoothEmulation
    from .protocol.browser.service import Browser
    from .protocol.css.service import CSS
    from .protocol.cache_storage.service import CacheStorage
    from .protocol.cast.service import Cast
    from .protocol.dom.service import DOM
    from .protocol.dom_debugger.service import DOMDebugger
    from .protocol.dom_snapshot.service import DOMSnapshot
    from .protocol.dom_storage.service import DOMStorage
    from .protocol.device_access.service import DeviceAccess
    from .protocol.device_orientation.service import DeviceOrientation
    from .protocol.emulation.service import Emulation
    from .protocol.event_breakpoints.service import EventBreakpoints
    from .protocol.extensions.service import Extensions
    from .protocol.fed_cm.service import FedCm
    from .protocol.fetch.service import Fetch
    from .protocol.file_system.service import FileSystem
    from .protocol.headless_experimental.service import HeadlessExperimental
    from .protocol.io.service import IO
    from .protocol.indexed_db.service import IndexedDB
    from .protocol.input.service import Input
    from .protocol.inspector.service import Inspector
    from .protocol.layer_tree.service import LayerTree
    from .protocol.log.service import Log
    from .protocol.media.service import Media
    from .protocol.memory.service import Memory
    from .protocol.network.service import Network
    from .protocol.overlay.service import Overlay
    from .protocol.pwa.service import PWA
    from .protocol.page.service import Page
    from .protocol.performance.service import Performance
    from .protocol.performance_timeline.service import PerformanceTimeline
    from .protocol.preload.service import Preload
    from .protocol.security.service import Security
    from .protocol.service_worker.service import ServiceWorker
    from .protocol.smart_card_emulation.service import SmartCardEmulation
    from .protocol.storage.service import Storage
    from .protocol.system_info.service import SystemInfo
    from .protocol.target.service import Target
    from .protocol.tethering.service import Tethering
    from .protocol.tracing.service import Tracing
    from .protocol.web_audio.service import WebAudio
    from .protocol.web_authn.service import WebAuthn
    from .protocol.debugger.service import Debugger
    from .protocol.heap_profiler.service import HeapProfiler
    from .protocol.profiler.service import Profiler
    from .protocol.runtime.service import Runtime

class Domains:
    """
    Collection of all CDP domains.
    
    This class acts as a container for all available CDP domain services. 
    Each domain is lazily initialized when first accessed.
    """
    def __init__(self, client: "Client"):
        """
        Initialize the Domains container.
        
        Args:
            client ("Client"): The parent CDP client instance.
        """
        self.client = client
        self._accessibility: Optional['Accessibility'] = None
        self._animation: Optional['Animation'] = None
        self._audits: Optional['Audits'] = None
        self._autofill: Optional['Autofill'] = None
        self._background_service: Optional['BackgroundService'] = None
        self._bluetooth_emulation: Optional['BluetoothEmulation'] = None
        self._browser: Optional['Browser'] = None
        self._css: Optional['CSS'] = None
        self._cache_storage: Optional['CacheStorage'] = None
        self._cast: Optional['Cast'] = None
        self._dom: Optional['DOM'] = None
        self._dom_debugger: Optional['DOMDebugger'] = None
        self._dom_snapshot: Optional['DOMSnapshot'] = None
        self._dom_storage: Optional['DOMStorage'] = None
        self._device_access: Optional['DeviceAccess'] = None
        self._device_orientation: Optional['DeviceOrientation'] = None
        self._emulation: Optional['Emulation'] = None
        self._event_breakpoints: Optional['EventBreakpoints'] = None
        self._extensions: Optional['Extensions'] = None
        self._fed_cm: Optional['FedCm'] = None
        self._fetch: Optional['Fetch'] = None
        self._file_system: Optional['FileSystem'] = None
        self._headless_experimental: Optional['HeadlessExperimental'] = None
        self._io: Optional['IO'] = None
        self._indexed_db: Optional['IndexedDB'] = None
        self._input: Optional['Input'] = None
        self._inspector: Optional['Inspector'] = None
        self._layer_tree: Optional['LayerTree'] = None
        self._log: Optional['Log'] = None
        self._media: Optional['Media'] = None
        self._memory: Optional['Memory'] = None
        self._network: Optional['Network'] = None
        self._overlay: Optional['Overlay'] = None
        self._pwa: Optional['PWA'] = None
        self._page: Optional['Page'] = None
        self._performance: Optional['Performance'] = None
        self._performance_timeline: Optional['PerformanceTimeline'] = None
        self._preload: Optional['Preload'] = None
        self._security: Optional['Security'] = None
        self._service_worker: Optional['ServiceWorker'] = None
        self._smart_card_emulation: Optional['SmartCardEmulation'] = None
        self._storage: Optional['Storage'] = None
        self._system_info: Optional['SystemInfo'] = None
        self._target: Optional['Target'] = None
        self._tethering: Optional['Tethering'] = None
        self._tracing: Optional['Tracing'] = None
        self._web_audio: Optional['WebAudio'] = None
        self._web_authn: Optional['WebAuthn'] = None
        self._debugger: Optional['Debugger'] = None
        self._heap_profiler: Optional['HeapProfiler'] = None
        self._profiler: Optional['Profiler'] = None
        self._runtime: Optional['Runtime'] = None

    @property
    def accessibility(self) -> 'Accessibility':
        """
Access the Accessibility domain.        """
        if self._accessibility is None:
            from .protocol.accessibility.service import Accessibility
            self._accessibility = Accessibility(client=self.client)
        return self._accessibility

    @property
    def animation(self) -> 'Animation':
        """
Access the Animation domain.        """
        if self._animation is None:
            from .protocol.animation.service import Animation
            self._animation = Animation(client=self.client)
        return self._animation

    @property
    def audits(self) -> 'Audits':
        """
Audits domain allows investigation of page violations and possible improvements.        """
        if self._audits is None:
            from .protocol.audits.service import Audits
            self._audits = Audits(client=self.client)
        return self._audits

    @property
    def autofill(self) -> 'Autofill':
        """
Defines commands and events for Autofill.        """
        if self._autofill is None:
            from .protocol.autofill.service import Autofill
            self._autofill = Autofill(client=self.client)
        return self._autofill

    @property
    def background_service(self) -> 'BackgroundService':
        """
Defines events for background web platform features.        """
        if self._background_service is None:
            from .protocol.background_service.service import BackgroundService
            self._background_service = BackgroundService(client=self.client)
        return self._background_service

    @property
    def bluetooth_emulation(self) -> 'BluetoothEmulation':
        """
This domain allows configuring virtual Bluetooth devices to test the web-bluetooth API.        """
        if self._bluetooth_emulation is None:
            from .protocol.bluetooth_emulation.service import BluetoothEmulation
            self._bluetooth_emulation = BluetoothEmulation(client=self.client)
        return self._bluetooth_emulation

    @property
    def browser(self) -> 'Browser':
        """
The Browser domain defines methods and events for browser managing.        """
        if self._browser is None:
            from .protocol.browser.service import Browser
            self._browser = Browser(client=self.client)
        return self._browser

    @property
    def css(self) -> 'CSS':
        """
This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles) have an associated `id` used in subsequent operations on the related object. Each object type has a specific `id` structure, and those are not interchangeable between objects of different kinds. CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.        """
        if self._css is None:
            from .protocol.css.service import CSS
            self._css = CSS(client=self.client)
        return self._css

    @property
    def cache_storage(self) -> 'CacheStorage':
        """
Access the CacheStorage domain.        """
        if self._cache_storage is None:
            from .protocol.cache_storage.service import CacheStorage
            self._cache_storage = CacheStorage(client=self.client)
        return self._cache_storage

    @property
    def cast(self) -> 'Cast':
        """
A domain for interacting with Cast, Presentation API, and Remote Playback API functionalities.        """
        if self._cast is None:
            from .protocol.cast.service import Cast
            self._cast = Cast(client=self.client)
        return self._cast

    @property
    def dom(self) -> 'DOM':
        """
This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object that has an `id`. This `id` can be used to get additional information on the Node, resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events only for the nodes that are known to the client. Backend keeps track of the nodes that were sent to the client and never sends the same node twice. It is client's responsibility to collect information about the nodes that were sent to the client. Note that `iframe` owner elements will return corresponding document elements as their child nodes.        """
        if self._dom is None:
            from .protocol.dom.service import DOM
            self._dom = DOM(client=self.client)
        return self._dom

    @property
    def dom_debugger(self) -> 'DOMDebugger':
        """
DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript execution will stop on these operations as if there was a regular breakpoint set.        """
        if self._dom_debugger is None:
            from .protocol.dom_debugger.service import DOMDebugger
            self._dom_debugger = DOMDebugger(client=self.client)
        return self._dom_debugger

    @property
    def dom_snapshot(self) -> 'DOMSnapshot':
        """
This domain facilitates obtaining document snapshots with DOM, layout, and style information.        """
        if self._dom_snapshot is None:
            from .protocol.dom_snapshot.service import DOMSnapshot
            self._dom_snapshot = DOMSnapshot(client=self.client)
        return self._dom_snapshot

    @property
    def dom_storage(self) -> 'DOMStorage':
        """
Query and modify DOM storage.        """
        if self._dom_storage is None:
            from .protocol.dom_storage.service import DOMStorage
            self._dom_storage = DOMStorage(client=self.client)
        return self._dom_storage

    @property
    def device_access(self) -> 'DeviceAccess':
        """
Access the DeviceAccess domain.        """
        if self._device_access is None:
            from .protocol.device_access.service import DeviceAccess
            self._device_access = DeviceAccess(client=self.client)
        return self._device_access

    @property
    def device_orientation(self) -> 'DeviceOrientation':
        """
Access the DeviceOrientation domain.        """
        if self._device_orientation is None:
            from .protocol.device_orientation.service import DeviceOrientation
            self._device_orientation = DeviceOrientation(client=self.client)
        return self._device_orientation

    @property
    def emulation(self) -> 'Emulation':
        """
This domain emulates different environments for the page.        """
        if self._emulation is None:
            from .protocol.emulation.service import Emulation
            self._emulation = Emulation(client=self.client)
        return self._emulation

    @property
    def event_breakpoints(self) -> 'EventBreakpoints':
        """
EventBreakpoints permits setting JavaScript breakpoints on operations and events occurring in native code invoked from JavaScript. Once breakpoint is hit, it is reported through Debugger domain, similarly to regular breakpoints being hit.        """
        if self._event_breakpoints is None:
            from .protocol.event_breakpoints.service import EventBreakpoints
            self._event_breakpoints = EventBreakpoints(client=self.client)
        return self._event_breakpoints

    @property
    def extensions(self) -> 'Extensions':
        """
Defines commands and events for browser extensions.        """
        if self._extensions is None:
            from .protocol.extensions.service import Extensions
            self._extensions = Extensions(client=self.client)
        return self._extensions

    @property
    def fed_cm(self) -> 'FedCm':
        """
This domain allows interacting with the FedCM dialog.        """
        if self._fed_cm is None:
            from .protocol.fed_cm.service import FedCm
            self._fed_cm = FedCm(client=self.client)
        return self._fed_cm

    @property
    def fetch(self) -> 'Fetch':
        """
A domain for letting clients substitute browser's network layer with client code.        """
        if self._fetch is None:
            from .protocol.fetch.service import Fetch
            self._fetch = Fetch(client=self.client)
        return self._fetch

    @property
    def file_system(self) -> 'FileSystem':
        """
Access the FileSystem domain.        """
        if self._file_system is None:
            from .protocol.file_system.service import FileSystem
            self._file_system = FileSystem(client=self.client)
        return self._file_system

    @property
    def headless_experimental(self) -> 'HeadlessExperimental':
        """
This domain provides experimental commands only supported in headless mode.        """
        if self._headless_experimental is None:
            from .protocol.headless_experimental.service import HeadlessExperimental
            self._headless_experimental = HeadlessExperimental(client=self.client)
        return self._headless_experimental

    @property
    def io(self) -> 'IO':
        """
Input/Output operations for streams produced by DevTools.        """
        if self._io is None:
            from .protocol.io.service import IO
            self._io = IO(client=self.client)
        return self._io

    @property
    def indexed_db(self) -> 'IndexedDB':
        """
Access the IndexedDB domain.        """
        if self._indexed_db is None:
            from .protocol.indexed_db.service import IndexedDB
            self._indexed_db = IndexedDB(client=self.client)
        return self._indexed_db

    @property
    def input(self) -> 'Input':
        """
Access the Input domain.        """
        if self._input is None:
            from .protocol.input.service import Input
            self._input = Input(client=self.client)
        return self._input

    @property
    def inspector(self) -> 'Inspector':
        """
Access the Inspector domain.        """
        if self._inspector is None:
            from .protocol.inspector.service import Inspector
            self._inspector = Inspector(client=self.client)
        return self._inspector

    @property
    def layer_tree(self) -> 'LayerTree':
        """
Access the LayerTree domain.        """
        if self._layer_tree is None:
            from .protocol.layer_tree.service import LayerTree
            self._layer_tree = LayerTree(client=self.client)
        return self._layer_tree

    @property
    def log(self) -> 'Log':
        """
Provides access to log entries.        """
        if self._log is None:
            from .protocol.log.service import Log
            self._log = Log(client=self.client)
        return self._log

    @property
    def media(self) -> 'Media':
        """
This domain allows detailed inspection of media elements.        """
        if self._media is None:
            from .protocol.media.service import Media
            self._media = Media(client=self.client)
        return self._media

    @property
    def memory(self) -> 'Memory':
        """
Access the Memory domain.        """
        if self._memory is None:
            from .protocol.memory.service import Memory
            self._memory = Memory(client=self.client)
        return self._memory

    @property
    def network(self) -> 'Network':
        """
Network domain allows tracking network activities of the page. It exposes information about http, file, data and other requests and responses, their headers, bodies, timing, etc.        """
        if self._network is None:
            from .protocol.network.service import Network
            self._network = Network(client=self.client)
        return self._network

    @property
    def overlay(self) -> 'Overlay':
        """
This domain provides various functionality related to drawing atop the inspected page.        """
        if self._overlay is None:
            from .protocol.overlay.service import Overlay
            self._overlay = Overlay(client=self.client)
        return self._overlay

    @property
    def pwa(self) -> 'PWA':
        """
This domain allows interacting with the browser to control PWAs.        """
        if self._pwa is None:
            from .protocol.pwa.service import PWA
            self._pwa = PWA(client=self.client)
        return self._pwa

    @property
    def page(self) -> 'Page':
        """
Actions and events related to the inspected page belong to the page domain.        """
        if self._page is None:
            from .protocol.page.service import Page
            self._page = Page(client=self.client)
        return self._page

    @property
    def performance(self) -> 'Performance':
        """
Access the Performance domain.        """
        if self._performance is None:
            from .protocol.performance.service import Performance
            self._performance = Performance(client=self.client)
        return self._performance

    @property
    def performance_timeline(self) -> 'PerformanceTimeline':
        """
Reporting of performance timeline events, as specified in https://w3c.github.io/performance-timeline/#dom-performanceobserver.        """
        if self._performance_timeline is None:
            from .protocol.performance_timeline.service import PerformanceTimeline
            self._performance_timeline = PerformanceTimeline(client=self.client)
        return self._performance_timeline

    @property
    def preload(self) -> 'Preload':
        """
Access the Preload domain.        """
        if self._preload is None:
            from .protocol.preload.service import Preload
            self._preload = Preload(client=self.client)
        return self._preload

    @property
    def security(self) -> 'Security':
        """
Access the Security domain.        """
        if self._security is None:
            from .protocol.security.service import Security
            self._security = Security(client=self.client)
        return self._security

    @property
    def service_worker(self) -> 'ServiceWorker':
        """
Access the ServiceWorker domain.        """
        if self._service_worker is None:
            from .protocol.service_worker.service import ServiceWorker
            self._service_worker = ServiceWorker(client=self.client)
        return self._service_worker

    @property
    def smart_card_emulation(self) -> 'SmartCardEmulation':
        """
Access the SmartCardEmulation domain.        """
        if self._smart_card_emulation is None:
            from .protocol.smart_card_emulation.service import SmartCardEmulation
            self._smart_card_emulation = SmartCardEmulation(client=self.client)
        return self._smart_card_emulation

    @property
    def storage(self) -> 'Storage':
        """
Access the Storage domain.        """
        if self._storage is None:
            from .protocol.storage.service import Storage
            self._storage = Storage(client=self.client)
        return self._storage

    @property
    def system_info(self) -> 'SystemInfo':
        """
The SystemInfo domain defines methods and events for querying low-level system information.        """
        if self._system_info is None:
            from .protocol.system_info.service import SystemInfo
            self._system_info = SystemInfo(client=self.client)
        return self._system_info

    @property
    def target(self) -> 'Target':
        """
Supports additional targets discovery and allows to attach to them.        """
        if self._target is None:
            from .protocol.target.service import Target
            self._target = Target(client=self.client)
        return self._target

    @property
    def tethering(self) -> 'Tethering':
        """
The Tethering domain defines methods and events for browser port binding.        """
        if self._tethering is None:
            from .protocol.tethering.service import Tethering
            self._tethering = Tethering(client=self.client)
        return self._tethering

    @property
    def tracing(self) -> 'Tracing':
        """
Access the Tracing domain.        """
        if self._tracing is None:
            from .protocol.tracing.service import Tracing
            self._tracing = Tracing(client=self.client)
        return self._tracing

    @property
    def web_audio(self) -> 'WebAudio':
        """
This domain allows inspection of Web Audio API. https://webaudio.github.io/web-audio-api/        """
        if self._web_audio is None:
            from .protocol.web_audio.service import WebAudio
            self._web_audio = WebAudio(client=self.client)
        return self._web_audio

    @property
    def web_authn(self) -> 'WebAuthn':
        """
This domain allows configuring virtual authenticators to test the WebAuthn API.        """
        if self._web_authn is None:
            from .protocol.web_authn.service import WebAuthn
            self._web_authn = WebAuthn(client=self.client)
        return self._web_authn

    @property
    def debugger(self) -> 'Debugger':
        """
Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing breakpoints, stepping through execution, exploring stack traces, etc.        """
        if self._debugger is None:
            from .protocol.debugger.service import Debugger
            self._debugger = Debugger(client=self.client)
        return self._debugger

    @property
    def heap_profiler(self) -> 'HeapProfiler':
        """
Access the HeapProfiler domain.        """
        if self._heap_profiler is None:
            from .protocol.heap_profiler.service import HeapProfiler
            self._heap_profiler = HeapProfiler(client=self.client)
        return self._heap_profiler

    @property
    def profiler(self) -> 'Profiler':
        """
Access the Profiler domain.        """
        if self._profiler is None:
            from .protocol.profiler.service import Profiler
            self._profiler = Profiler(client=self.client)
        return self._profiler

    @property
    def runtime(self) -> 'Runtime':
        """
Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects. Evaluation results are returned as mirror object that expose object type, string representation and unique identifier that can be used for further object reference. Original objects are maintained in memory unless they are either explicitly released or are released along with the other objects in their object group.        """
        if self._runtime is None:
            from .protocol.runtime.service import Runtime
            self._runtime = Runtime(client=self.client)
        return self._runtime