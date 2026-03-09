from src.agent.session.views import BrowserState, Tab
from src.agent.dom.views import DOMElementNode, DOMState
from src.agent.browser import Browser
from collections import deque
from pathlib import Path
from typing import Any
import asyncio
import base64
import json





_SPECIAL_KEYS: dict[str, dict] = {
    'Enter':     {'key': 'Enter',     'code': 'Enter',      'keyCode': 13},
    'Escape':    {'key': 'Escape',    'code': 'Escape',     'keyCode': 27},
    'Tab':       {'key': 'Tab',       'code': 'Tab',        'keyCode': 9},
    'Backspace': {'key': 'Backspace', 'code': 'Backspace',  'keyCode': 8},
    'Delete':    {'key': 'Delete',    'code': 'Delete',     'keyCode': 46},
    'PageUp':    {'key': 'PageUp',    'code': 'PageUp',     'keyCode': 33},
    'PageDown':  {'key': 'PageDown',  'code': 'PageDown',   'keyCode': 34},
    'ArrowUp':   {'key': 'ArrowUp',   'code': 'ArrowUp',    'keyCode': 38},
    'ArrowDown': {'key': 'ArrowDown', 'code': 'ArrowDown',  'keyCode': 40},
    'ArrowLeft': {'key': 'ArrowLeft', 'code': 'ArrowLeft',  'keyCode': 37},
    'ArrowRight':{'key': 'ArrowRight','code': 'ArrowRight', 'keyCode': 39},
    'Home':      {'key': 'Home',      'code': 'Home',       'keyCode': 36},
    'End':       {'key': 'End',       'code': 'End',        'keyCode': 35},
    'F5':        {'key': 'F5',        'code': 'F5',         'keyCode': 116},
    ' ':         {'key': ' ',         'code': 'Space',      'keyCode': 32},
    'Space':     {'key': ' ',         'code': 'Space',      'keyCode': 32},
}

_MODIFIER_KEYS: dict[str, dict] = {
    'Control': {'key': 'Control', 'code': 'ControlLeft', 'keyCode': 17, 'bit': 2},
    'Ctrl':    {'key': 'Control', 'code': 'ControlLeft', 'keyCode': 17, 'bit': 2},
    'Shift':   {'key': 'Shift',   'code': 'ShiftLeft',   'keyCode': 16, 'bit': 8},
    'Alt':     {'key': 'Alt',     'code': 'AltLeft',     'keyCode': 18, 'bit': 1},
    'Meta':    {'key': 'Meta',    'code': 'MetaLeft',    'keyCode': 91, 'bit': 4},
    'Command': {'key': 'Meta',    'code': 'MetaLeft',    'keyCode': 91, 'bit': 4},
}


def _parse_key_combo(keys_str: str):
    parts = [p.strip() for p in keys_str.split('+')]
    mods = [_MODIFIER_KEYS[p] for p in parts[:-1] if p in _MODIFIER_KEYS]
    return mods, parts[-1]


class Session:
    def __init__(self, browser: Browser):
        self.browser = browser

        # CDP session state
        self._targets:    dict[str, dict]           = {}
        self._sessions:   dict[str, str]            = {}
        self._lifecycle:  dict[str, deque]          = {}
        self._page_ready: dict[str, asyncio.Event]  = {}
        self._current_target_id: str | None         = None

        self._browser_state: BrowserState = None

        # Watchdogs (attached during init_session)
        from src.agent.watchdog import DialogWatchdog, CrashWatchdog, DownloadWatchdog
        self._watchdogs = [
            DialogWatchdog(self),
            CrashWatchdog(self),
            DownloadWatchdog(self),
        ]

    # ------------------------------------------------------------------
    # Session init / teardown
    # ------------------------------------------------------------------

    async def init_session(self):
        await self.browser.get_cdp_client()

        self.browser.on('Target.attachedToTarget',   self._on_attached)
        self.browser.on('Target.detachedFromTarget', self._on_detached)
        self.browser.on('Target.targetInfoChanged',  self._on_target_info_changed)
        self.browser.on('Page.lifecycleEvent',       self._on_lifecycle_event)

        for watchdog in self._watchdogs:
            await watchdog.attach()

        await self.browser.send('Target.setAutoAttach', {
            'autoAttach': True, 'waitForDebuggerOnStart': False, 'flatten': True,
        })
        await self.browser.send('Target.setDiscoverTargets', {
            'discover': True, 'filter': [{'type': 'page'}],
        })

        result = await self.browser.send('Target.getTargets', {'filter': [{'type': 'page'}]})
        page_targets = result.get('targetInfos', [])

        if page_targets:
            self._current_target_id = page_targets[0]['targetId']
            for info in page_targets:
                tid = info['targetId']
                attach = await self.browser.send('Target.attachToTarget', {'targetId': tid, 'flatten': True})
                sid = attach['sessionId']
                self._targets[tid]   = {'url': info['url'], 'title': info.get('title', '')}
                self._sessions[tid]  = sid
                self._lifecycle[sid] = deque(maxlen=50)
                await self._init_session_domains(sid)
        else:
            r = await self.browser.send('Target.createTarget', {'url': 'about:blank'})
            self._current_target_id = r['targetId']
            attach = await self.browser.send('Target.attachToTarget', {
                'targetId': self._current_target_id, 'flatten': True,
            })
            sid = attach['sessionId']
            self._targets[self._current_target_id]  = {'url': 'about:blank', 'title': ''}
            self._sessions[self._current_target_id] = sid
            self._lifecycle[sid] = deque(maxlen=50)
            await self._init_session_domains(sid)

    async def _init_session_domains(self, session_id: str):
        await asyncio.gather(
            self.browser.send('Page.enable',    {}, session_id=session_id),
            self.browser.send('Runtime.enable', {}, session_id=session_id),
            self.browser.send('Network.enable', {}, session_id=session_id),
        )
        await self.browser.send('Page.setLifecycleEventsEnabled',
                                {'enabled': True}, session_id=session_id)
        await self.browser.send('Target.setAutoAttach', {
            'autoAttach': True, 'waitForDebuggerOnStart': False, 'flatten': True,
        }, session_id=session_id)

        with open('./src/agent/session/script.js') as f:
            anti_detect = f.read()
        try:
            await self.browser.send('Page.addScriptToEvaluateOnNewDocument',
                                    {'source': anti_detect}, session_id=session_id)
        except Exception:
            pass
        try:
            await self.browser.send('Runtime.evaluate', {
                'expression': anti_detect, 'returnByValue': False,
            }, session_id=session_id)
        except Exception:
            pass

    async def close_session(self):
        try:
            for target_id, session_id in list(self._sessions.items()):
                try:
                    await self.browser.send('Target.closeTarget',
                                            {'targetId': target_id}, session_id=session_id)
                except Exception:
                    pass
        except Exception:
            pass
        finally:
            self._targets.clear()
            self._sessions.clear()
            self._lifecycle.clear()
            for ev in self._page_ready.values():
                ev.set()
            self._page_ready.clear()
            self._current_target_id = None
        await self.browser.close_browser()

    # ------------------------------------------------------------------
    # CDP event handlers
    # ------------------------------------------------------------------

    async def _on_attached(self, event, _=None):
        info = event.get('targetInfo', {})
        target_id  = info.get('targetId')
        session_id = event.get('sessionId')
        if not target_id or not session_id:
            return
        if target_id in self._sessions:
            return
        if info.get('type', '') != 'page':
            return
        self._targets[target_id]    = {'url': info.get('url', ''), 'title': info.get('title', '')}
        self._sessions[target_id]   = session_id
        self._lifecycle[session_id] = deque(maxlen=50)
        await self._init_session_domains(session_id)

    def _on_detached(self, event, _=None):
        session_id = event.get('sessionId')
        target_id  = next((t for t, s in self._sessions.items() if s == session_id), None)
        if target_id:
            self._targets.pop(target_id, None)
            self._sessions.pop(target_id, None)
            self._lifecycle.pop(session_id, None)
            ready = self._page_ready.pop(session_id, None)
            if ready:
                ready.set()  # unblock any waiter on a closing tab
            if self._current_target_id == target_id and self._sessions:
                self._current_target_id = next(iter(self._sessions))

    def _on_target_info_changed(self, event, _=None):
        info = event.get('targetInfo', {})
        tid  = info.get('targetId')
        if tid in self._targets:
            self._targets[tid]['url']   = info.get('url', '')
            self._targets[tid]['title'] = info.get('title', '')

    def _on_lifecycle_event(self, event, session_id=None):
        if not session_id:
            return
        name = event.get('name', '')
        if session_id in self._lifecycle:
            self._lifecycle[session_id].append({
                'name': name, 'loaderId': event.get('loaderId'),
                'timestamp': event.get('timestamp'),
            })
        # Signal any waiter on networkIdle or load
        if name in ('networkIdle', 'load'):
            ready = self._page_ready.get(session_id)
            if ready:
                ready.set()

    # ------------------------------------------------------------------
    # Session helpers
    # ------------------------------------------------------------------

    def _get_current_session_id(self) -> str | None:
        return self._sessions.get(self._current_target_id)

    # ------------------------------------------------------------------
    # Tabs
    # ------------------------------------------------------------------

    async def get_all_tabs(self) -> list[Tab]:
        tabs = []
        for i, (tid, info) in enumerate(self._targets.items()):
            sid = self._sessions.get(tid, '')
            try:
                result = await self.browser.send('Runtime.evaluate', {
                    'expression': '({url: document.URL, title: document.title})',
                    'returnByValue': True,
                }, session_id=sid)
                live  = result.get('result', {}).get('value', {})
                url   = live.get('url',   info.get('url', ''))
                title = live.get('title', info.get('title', ''))
                self._targets[tid]['url']   = url
                self._targets[tid]['title'] = title
            except Exception:
                url   = info.get('url', '')
                title = info.get('title', '')
            tabs.append(Tab(id=i, url=url, title=title, target_id=tid, session_id=sid))
        return tabs

    async def get_current_tab(self) -> Tab | None:
        if not self._current_target_id:
            return None
        tid  = self._current_target_id
        sid  = self._sessions.get(tid, '')
        info = self._targets.get(tid, {})
        try:
            result = await self.browser.send('Runtime.evaluate', {
                'expression': '({url: document.URL, title: document.title})',
                'returnByValue': True,
            }, session_id=sid)
            live  = result.get('result', {}).get('value', {})
            url   = live.get('url',   info.get('url', ''))
            title = live.get('title', info.get('title', ''))
        except Exception:
            url   = info.get('url', '')
            title = info.get('title', '')
        tabs = await self.get_all_tabs()
        idx  = next((t.id for t in tabs if t.target_id == tid), 0)
        return Tab(id=idx, url=url, title=title, target_id=tid, session_id=sid)

    async def new_tab(self) -> Tab:
        r = await self.browser.send('Target.createTarget', {'url': 'about:blank'})
        tid    = r['targetId']
        attach = await self.browser.send('Target.attachToTarget', {'targetId': tid, 'flatten': True})
        sid = attach['sessionId']
        self._targets[tid]   = {'url': 'about:blank', 'title': ''}
        self._sessions[tid]  = sid
        self._lifecycle[sid] = deque(maxlen=50)
        await self._init_session_domains(sid)
        self._current_target_id = tid
        await self._activate_target(tid)
        return Tab(id=len(self._targets) - 1, url='about:blank', title='', target_id=tid, session_id=sid)

    async def close_tab(self, target_id: str = None):
        tid = target_id or self._current_target_id
        sid = self._sessions.get(tid)
        if len(self._sessions) <= 1:
            return
        try:
            await self.browser.send('Target.closeTarget', {'targetId': tid}, session_id=sid)
        except Exception:
            pass
        remaining = [t for t in self._sessions if t != tid]
        if remaining and self._current_target_id == tid:
            self._current_target_id = remaining[-1]
            await self._activate_target(remaining[-1])

    async def switch_tab(self, tab_index: int):
        tabs = await self.get_all_tabs()
        if tab_index < 0 or tab_index >= len(tabs):
            raise IndexError(f'Tab index {tab_index} out of range ({len(tabs)} tabs)')
        self._current_target_id = tabs[tab_index].target_id
        await self._activate_target(self._current_target_id)

    async def _activate_target(self, target_id: str):
        try:
            await self.browser.send('Target.activateTarget', {'targetId': target_id})
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    async def navigate(self, url: str):
        sid = self._get_current_session_id()
        # Clear stale lifecycle events and arm the ready event before navigating
        if sid:
            if sid in self._lifecycle:
                self._lifecycle[sid].clear()
            self._page_ready.pop(sid, None)
        await self.browser.send('Page.navigate', {
            'url': url, 'transitionType': 'address_bar',
        }, session_id=sid)
        await self._wait_for_page(timeout=15.0)

    async def go_back(self):
        await self.execute_script('history.back()')
        await self._wait_for_page(timeout=10.0)

    async def go_forward(self):
        await self.execute_script('history.forward()')
        await self._wait_for_page(timeout=10.0)

    async def _wait_for_page(self, timeout: float = 10.0):
        sid = self._get_current_session_id()
        if not sid:
            return

        # Arm an asyncio.Event that _on_lifecycle_event will set on networkIdle/load
        ready = asyncio.Event()
        self._page_ready[sid] = ready

        try:
            await asyncio.wait_for(ready.wait(), timeout=timeout)
        except asyncio.TimeoutError:
            pass
        finally:
            self._page_ready.pop(sid, None)

        await asyncio.sleep(0.3)  # brief render buffer

    # ------------------------------------------------------------------
    # Script execution
    # ------------------------------------------------------------------

    async def execute_script(self, script: str) -> Any:
        sid = self._get_current_session_id()
        try:
            result = await self.browser.send('Runtime.evaluate', {
                'expression': script, 'returnByValue': True, 'awaitPromise': True,
            }, session_id=sid)
            if result and 'result' in result:
                return result['result'].get('value')
        except Exception as e:
            print(f'execute_script error: {e}')
        return None

    # ------------------------------------------------------------------
    # Input
    # ------------------------------------------------------------------

    async def click_at(self, x: int, y: int):
        sid = self._get_current_session_id()
        for event_type in ('mousePressed', 'mouseReleased'):
            await self.browser.send('Input.dispatchMouseEvent', {
                'type': event_type, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1,
            }, session_id=sid)

    async def scroll_into_view(self, xpath: str):
        escaped = xpath.replace('"', '\\"')
        await self.execute_script(
            f'(function(){{'
            f'  var el = document.evaluate("{escaped}", document, null, 8, null).singleNodeValue;'
            f'  if (el) el.scrollIntoView({{block:"center", inline:"nearest"}});'
            f'}})()'
        )

    async def type_text(self, text: str, delay_ms: int = 50):
        sid = self._get_current_session_id()
        for char in text:
            await self.browser.send('Input.dispatchKeyEvent', {
                'type': 'char', 'text': char,
            }, session_id=sid)
            if delay_ms:
                await asyncio.sleep(delay_ms / 1000)

    async def key_press(self, keys: str):
        sid = self._get_current_session_id()
        mods, key_name = _parse_key_combo(keys)
        combined = sum(m['bit'] for m in mods)

        key_def = _SPECIAL_KEYS.get(key_name)
        if key_def is None:
            if len(key_name) == 1:
                key_def = {'key': key_name, 'code': f'Key{key_name.upper()}', 'keyCode': ord(key_name.upper())}
            else:
                key_def = {'key': key_name, 'code': key_name, 'keyCode': 0}

        for mod in mods:
            await self.browser.send('Input.dispatchKeyEvent', {
                'type': 'rawKeyDown', 'key': mod['key'], 'code': mod['code'],
                'windowsVirtualKeyCode': mod['keyCode'], 'modifiers': combined,
            }, session_id=sid)

        await self.browser.send('Input.dispatchKeyEvent', {
            'type': 'rawKeyDown', 'key': key_def['key'], 'code': key_def['code'],
            'windowsVirtualKeyCode': key_def.get('keyCode', 0), 'modifiers': combined,
        }, session_id=sid)
        await self.browser.send('Input.dispatchKeyEvent', {
            'type': 'keyUp', 'key': key_def['key'], 'code': key_def['code'],
            'windowsVirtualKeyCode': key_def.get('keyCode', 0), 'modifiers': combined,
        }, session_id=sid)

        for mod in reversed(mods):
            await self.browser.send('Input.dispatchKeyEvent', {
                'type': 'keyUp', 'key': mod['key'], 'code': mod['code'],
                'windowsVirtualKeyCode': mod['keyCode'], 'modifiers': 0,
            }, session_id=sid)

    async def scroll_page(self, direction: str, amount: int = 500):
        sid = self._get_current_session_id()
        viewport = await self.get_viewport()
        cx = viewport[0] // 2
        cy = viewport[1] // 2
        delta = -amount if direction == 'up' else amount
        await self.browser.send('Input.dispatchMouseEvent', {
            'type': 'mouseWheel', 'x': cx, 'y': cy, 'deltaX': 0, 'deltaY': delta,
        }, session_id=sid)

    async def scroll_element(self, xpath: str, direction: str, amount: int = 500):
        escaped = xpath.replace('"', '\\"')
        delta = -amount if direction == 'up' else amount
        await self.execute_script(
            f'(function(){{'
            f'  var el = document.evaluate("{escaped}", document, null, 8, null).singleNodeValue;'
            f'  if (el) el.scrollBy(0, {delta});'
            f'}})()'
        )

    async def get_scroll_position(self) -> dict:
        result = await self.execute_script(
            '({scrollY: window.scrollY, scrollHeight: document.documentElement.scrollHeight, innerHeight: window.innerHeight})'
        )
        return result or {'scrollY': 0, 'scrollHeight': 0, 'innerHeight': 0}

    # ------------------------------------------------------------------
    # Screenshot / page info
    # ------------------------------------------------------------------

    async def get_screenshot(self, full_page: bool = False, save_screenshot: bool = False) -> bytes | None:
        sid = self._get_current_session_id()
        await asyncio.sleep(0.3)
        try:
            result = await self.browser.send('Page.captureScreenshot', {
                'format': 'jpeg', 'quality': 80, 'captureBeyondViewport': full_page,
            }, session_id=sid)
            data = base64.b64decode(result['data'])
        except Exception as e:
            print(f'Screenshot failed: {e}')
            return None

        if save_screenshot:
            from datetime import datetime
            folder_path = Path('./screenshots')
            folder_path.mkdir(parents=True, exist_ok=True)
            path = folder_path / f'screenshot_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.jpeg'
            with open(path, 'wb') as f:
                f.write(data)
        return data

    async def get_page_content(self) -> str:
        return await self.execute_script('document.documentElement.outerHTML') or ''

    async def get_viewport(self) -> tuple[int, int]:
        result = await self.execute_script('({width: window.innerWidth, height: window.innerHeight})')
        if isinstance(result, dict):
            return result.get('width', 1280), result.get('height', 720)
        return 1280, 720

    # ------------------------------------------------------------------
    # Element actions
    # ------------------------------------------------------------------

    async def set_file_input(self, xpath: str, files: list[str]):
        sid = self._get_current_session_id()
        escaped = xpath.replace('"', '\\"')
        result = await self.browser.send('Runtime.evaluate', {
            'expression': f'document.evaluate("{escaped}", document, null, 8, null).singleNodeValue',
            'returnByValue': False,
        }, session_id=sid)
        obj_id = result.get('result', {}).get('objectId')
        if not obj_id:
            raise Exception(f'Could not resolve file input element at xpath: {xpath}')
        node = await self.browser.send('DOM.describeNode', {'objectId': obj_id}, session_id=sid)
        backend_node_id = node['node']['backendNodeId']
        await self.browser.send('DOM.setFileInputFiles', {
            'files': files, 'backendNodeId': backend_node_id,
        }, session_id=sid)

    async def select_option(self, xpath: str, labels: list[str]):
        escaped     = xpath.replace('"', '\\"')
        labels_json = json.dumps(labels)
        await self.execute_script(
            f'(function(){{'
            f'  var el = document.evaluate("{escaped}", document, null, 8, null).singleNodeValue;'
            f'  if (!el) return false;'
            f'  var labels = {labels_json};'
            f'  for (var i = 0; i < el.options.length; i++) {{'
            f'    if (labels.includes(el.options[i].text.trim())) el.options[i].selected = true;'
            f'  }}'
            f'  el.dispatchEvent(new Event("change", {{bubbles: true}}));'
            f'  return true;'
            f'}})()'
        )

    # ------------------------------------------------------------------
    # DOM state
    # ------------------------------------------------------------------

    async def get_state(self, use_vision: bool = False) -> BrowserState:
        from src.agent.dom import DOM
        dom = DOM(session=self)
        screenshot, dom_state = await dom.get_state(use_vision=use_vision)
        tabs        = await self.get_all_tabs()
        current_tab = await self.get_current_tab()
        self._browser_state = BrowserState(
            current_tab=current_tab,
            tabs=tabs,
            screenshot=screenshot,
            dom_state=dom_state,
        )
        return self._browser_state

    async def get_element_by_index(self, index: int) -> DOMElementNode:
        selector_map = self._browser_state.dom_state.selector_map
        if index not in selector_map:
            raise Exception(f'Element at index {index} not found in selector map')
        return selector_map[index]
