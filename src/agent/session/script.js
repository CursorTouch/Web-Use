(() => {
  // 1. Remove webdriver flag
  Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined,
    configurable: true,
  });

  // 2. Languages
  Object.defineProperty(navigator, 'languages', {
    get: () => ['en-US', 'en'],
    configurable: true,
  });

  // 3. Vendor
  Object.defineProperty(navigator, 'vendor', {
    get: () => 'Google Inc.',
    configurable: true,
  });

  // 4. Platform
  Object.defineProperty(navigator, 'platform', {
    get: () => 'Win32',
    configurable: true,
  });

  // 5. Hardware concurrency
  Object.defineProperty(navigator, 'hardwareConcurrency', {
    get: () => 8,
    configurable: true,
  });

  // 6. Device memory
  Object.defineProperty(navigator, 'deviceMemory', {
    get: () => 8,
    configurable: true,
  });

  // 7. Max touch points (desktop = 0)
  Object.defineProperty(navigator, 'maxTouchPoints', {
    get: () => 0,
    configurable: true,
  });

  // 8. Realistic Chrome object
  window.chrome = {
    app: {
      isInstalled: false,
      InstallState: { DISABLED: 'disabled', INSTALLED: 'installed', NOT_INSTALLED: 'not_installed' },
      RunningState: { CANNOT_RUN: 'cannot_run', READY_TO_RUN: 'ready_to_run', RUNNING: 'running' },
    },
    runtime: {
      OnInstalledReason: { CHROME_UPDATE: 'chrome_update', INSTALL: 'install', SHARED_MODULE_UPDATE: 'shared_module_update', UPDATE: 'update' },
      OnRestartRequiredReason: { APP_UPDATE: 'app_update', GC: 'gc', OS_UPDATE: 'os_update' },
      PlatformArch: { ARM: 'arm', ARM64: 'arm64', MIPS: 'mips', MIPS64: 'mips64', X86_32: 'x86-32', X86_64: 'x86-64' },
      PlatformNaclArch: { ARM: 'arm', MIPS: 'mips', MIPS64: 'mips64', X86_32: 'x86-32', X86_64: 'x86-64' },
      PlatformOs: { ANDROID: 'android', CROS: 'cros', LINUX: 'linux', MAC: 'mac', OPENBSD: 'openbsd', WIN: 'win' },
      RequestUpdateCheckStatus: { NO_UPDATE: 'no_update', THROTTLED: 'throttled', UPDATE_AVAILABLE: 'update_available' },
    },
  };

  // 9. Permissions — handle notifications correctly, pass others through
  const _origPermQuery = window.navigator.permissions.query;
  window.navigator.permissions.query = (parameters) => (
    parameters.name === 'notifications'
      ? Promise.resolve({ state: Notification.permission })
      : _origPermQuery(parameters)
  );

  // 10. Canvas fingerprint noise — add imperceptible jitter to text rendering
  const _origGetContext = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (type, ...args) {
    const ctx = _origGetContext.call(this, type, ...args);
    if (type === '2d' && ctx) {
      const _origFillText = ctx.fillText.bind(ctx);
      ctx.fillText = function (text, x, y, ...rest) {
        ctx.shadowBlur = Math.random() * 0.02;
        return _origFillText(text, x, y, ...rest);
      };
      const _origStrokeText = ctx.strokeText.bind(ctx);
      ctx.strokeText = function (text, x, y, ...rest) {
        ctx.shadowBlur = Math.random() * 0.02;
        return _origStrokeText(text, x, y, ...rest);
      };
    }
    return ctx;
  };

  // 11. WebGL — spoof UNMASKED_VENDOR and UNMASKED_RENDERER
  const _webglParamHandler = {
    apply(target, ctx, args) {
      const param = args[0];
      if (param === 37445) return 'Intel Inc.';              // UNMASKED_VENDOR_WEBGL
      if (param === 37446) return 'Intel Iris OpenGL Engine'; // UNMASKED_RENDERER_WEBGL
      return Reflect.apply(target, ctx, args);
    },
  };
  try {
    WebGLRenderingContext.prototype.getParameter = new Proxy(
      WebGLRenderingContext.prototype.getParameter, _webglParamHandler
    );
  } catch (_) {}
  try {
    WebGL2RenderingContext.prototype.getParameter = new Proxy(
      WebGL2RenderingContext.prototype.getParameter, _webglParamHandler
    );
  } catch (_) {}

  // 12. Battery API — report always charging and full
  if (navigator.getBattery) {
    navigator.getBattery = () => Promise.resolve({
      charging: true,
      chargingTime: 0,
      dischargingTime: Infinity,
      level: 1.0,
      addEventListener() {},
      removeEventListener() {},
      dispatchEvent() { return true; },
    });
  }

  // 13. Network connection — report stable 4G
  try {
    Object.defineProperty(navigator, 'connection', {
      get: () => ({
        rtt: 100,
        downlink: 10,
        effectiveType: '4g',
        saveData: false,
        addEventListener() {},
        removeEventListener() {},
      }),
      configurable: true,
    });
  } catch (_) {}

  // 14. Clean up CDP / ChromeDriver artifacts leaked onto window
  try {
    Object.keys(window).forEach(key => {
      if (key.startsWith('cdc_') || key.startsWith('__cdc_')) {
        try { delete window[key]; } catch (_) {}
      }
    });
  } catch (_) {}
})();
