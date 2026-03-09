from .constant import BROWSER_PROTOCOL_URL, JS_PROTOCOL_URL
from .method_generator import MethodGenerator
from .event_generator import EventGenerator
from .type_generator import TypeGenerator
from .client_generator import ClientGenerator
from .domain_generator import DomainGenerator
from jinja2_strcase import StrcaseExtension
from jinja2 import Environment
from textwrap import dedent
from functools import cache
from pathlib import Path
from typing import Any, Optional
import inflection
import httpx

class CDPGenerator:    
    def __init__(self, src_path: Optional[Path] = None):
        if src_path is None:
            self.root_path = Path(__file__).parent.parent.parent.parent
            self.src_path = self.root_path / "src"
        else:
            self.src_path = src_path
            self.root_path = src_path.parent
            
        self.cdp_path = self.src_path / "cdp"
        self.protocol_path = self.cdp_path / "protocol"
        self.client_path = self.cdp_path
        
        self.protocol_package = "cdp.protocol"
        self.package_name = "cdp"
        
        self.method_generator = MethodGenerator(self.protocol_path, self.protocol_package)
        self.event_generator = EventGenerator(self.protocol_path, self.protocol_package)
        self.type_generator = TypeGenerator(self.protocol_path, self.protocol_package)
        self.domain_generator = DomainGenerator(self.method_generator, self.event_generator, self.package_name)
        self.client_generator = ClientGenerator(self.protocol_package, self.package_name)

    @property
    @cache
    def domains(self):
        domains = []
        for url in [BROWSER_PROTOCOL_URL, JS_PROTOCOL_URL]:
            try:
                protocol = httpx.get(url).json()
                domains.extend(protocol.get('domains', []))
            except Exception as e:
                print(f"Failed to load protocol from {url}: {e}")
        return domains

    def generate(self):
        # Create base directories and __init__.py files
        self.cdp_path.mkdir(parents=True, exist_ok=True)
        self.protocol_path.mkdir(parents=True, exist_ok=True)
        
        self.ensure_init(self.cdp_path)
        self.ensure_init(self.protocol_path)
        
        # Add py.typed to both cdp and cdp.protocol
        (self.cdp_path / "py.typed").write_text("")
        (self.protocol_path / "py.typed").write_text("")
        
        self.generate_protocol()
        self.generate_client()
        
    def ensure_init(self, path: Path):
        init_file = path / "__init__.py"
        if not init_file.exists():
            init_file.write_text("")

    def generate_protocol(self):
        for domain in self.domains:
            if not domain.get('deprecated', False):
                self.generate_domain_types(domain)
                self.generate_domain_services(domain)
    
    def generate_client(self):
        client_dir = self.client_path
        domains = list(filter(lambda x: not x.get('deprecated', False), self.domains))
        
        # Generate domains.py with Domains class
        domains_content = self.client_generator.generate_domains(domains)
        self.write_file(client_dir / "domains.py", domains_content)

        # Generate service.py with Client class
        service_content = self.client_generator.generate_service()
        self.write_file(client_dir / "service.py", service_content)
        
        # Generate cdp/__init__.py
        init_content = dedent("""
            from .domains import Domains
            from .service import Client
            
            __all__ = ["Domains", "Client"]
        """).strip()
        self.write_file(client_dir / "__init__.py", init_content)

    def generate_domain_services(self, domain: dict):
        domain_name_snake = inflection.underscore(domain['domain'])
        domain_dir = self.protocol_path / domain_name_snake
        
        methods_dir = domain_dir / "methods"
        events_dir = domain_dir / "events"
        
        domain_dir.mkdir(parents=True, exist_ok=True)
        methods_dir.mkdir(parents=True, exist_ok=True)
        events_dir.mkdir(parents=True, exist_ok=True)
        
        self.ensure_init(domain_dir)
        self.ensure_init(methods_dir)
        self.ensure_init(events_dir)
        
        # Generate methods service
        methods_content = self.domain_generator.generate_methods_service(domain)
        self.write_file(methods_dir / "service.py", methods_content)

        # Generate events service
        events_content = self.domain_generator.generate_events_service(domain)
        self.write_file(events_dir / "service.py", events_content)

        # Generate main service
        service_content = self.domain_generator.generate_domain_service(domain)
        self.write_file(domain_dir / "service.py", service_content)

    def generate_domain_types(self, domain: dict):
        domain_name_snake = inflection.underscore(domain['domain'])
        domain_dir = self.protocol_path / domain_name_snake
        
        methods_dir = domain_dir / "methods"
        events_dir = domain_dir / "events"
        
        domain_dir.mkdir(parents=True, exist_ok=True)
        methods_dir.mkdir(parents=True, exist_ok=True)
        events_dir.mkdir(parents=True, exist_ok=True)
        
        self.ensure_init(domain_dir)
        self.ensure_init(methods_dir)
        self.ensure_init(events_dir)

        # Generate types
        types_content = self.type_generator.generate_types(domain)
        self.write_file(domain_dir / "types.py", types_content)

        # Generate method types
        method_types_content = self.method_generator.generate_method_types(domain)
        self.write_file(methods_dir / "types.py", method_types_content)

        # Generate event types
        event_types_content = self.event_generator.generate_event_types(domain)
        self.write_file(events_dir / "types.py", event_types_content)

    def write_file(self, path: Path, content: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
