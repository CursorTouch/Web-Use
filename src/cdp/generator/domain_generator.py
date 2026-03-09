from jinja2 import Environment
from jinja2_strcase import StrcaseExtension
from .method_generator import MethodGenerator
from .event_generator import EventGenerator

METHODS_SERVICE_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Domain Methods\"\"\"
from __future__ import annotations
{% for import_ in imports %}
{{ import_ }}
{% endfor %}

if TYPE_CHECKING:
    from ....service import Client

class {{ class_name }}:
    \"\"\"
    Methods for the {{ domain_name }} domain.
    \"\"\"
    def __init__(self, client: Client):
        \"\"\"
        Initialize the {{ domain_name }} methods.
        
        Args:
            client (Client): The parent CDP client instance.
        \"\"\"
        self.client = client

    {% for implementation in method_implementations %}
    {{ implementation | indent(4) }}
    {% endfor %}
"""

EVENTS_SERVICE_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Domain Events\"\"\"
from __future__ import annotations
{% for import_ in imports %}
{{ import_ }}
{% endfor %}

if TYPE_CHECKING:
    from ....service import Client

class {{ class_name }}:
    \"\"\"
    Events for the {{ domain_name }} domain.
    \"\"\"
    def __init__(self, client: Client):
        \"\"\"
        Initialize the {{ domain_name }} events.
        
        Args:
            client (Client): The parent CDP client instance.
        \"\"\"
        self.client = client

    {% for implementation in event_implementations %}
    {{ implementation | indent(4) }}
    {% endfor %}
"""

DOMAIN_SERVICE_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Domain\"\"\"
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import {{ domain_name }}Methods
from .events.service import {{ domain_name }}Events

if TYPE_CHECKING:
    from ...service import Client

class {{ domain_name }}({{ domain_name }}Methods, {{ domain_name }}Events):
    \"\"\"
    {{ domain_description | replace("\\n", " ") }}
    \"\"\"
    def __init__(self, client: Client):
        \"\"\"
        Initialize the {{ domain_name }} domain.
        
        Args:
            client (Client): The parent CDP client instance.
        \"\"\"
        {{ domain_name }}Methods.__init__(self, client)
        {{ domain_name }}Events.__init__(self, client)
"""

class DomainGenerator:
    def __init__(self, method_generator: MethodGenerator, event_generator: EventGenerator, package_name: str):
        self.method_generator = method_generator
        self.event_generator = event_generator
        self.package_name = package_name
        self.env = Environment(trim_blocks=True, lstrip_blocks=True, extensions=[StrcaseExtension])

    def generate_methods_service(self, domain: dict) -> str:
        domain_name = domain['domain']
        self.method_generator.current_domain = domain_name
        self.method_generator.clear()
        
        methods = domain.get('commands', [])
        method_implementations = []
        for method in methods:
            if not method.get('deprecated', False):
                code = self.method_generator.generate_method_implementation(method)
                method_implementations.append(code)

        imports = self.method_generator.imports.copy()
        imports.update(self.method_generator.type_checking_imports)
        imports.add("from .types import *")
        imports.add("from ..types import *") # Import shared types
        imports.add("from typing import Optional, Dict, Any, Callable, TYPE_CHECKING")
        
        class_name = f"{domain_name}Methods"
        template = self.env.from_string(METHODS_SERVICE_TEMPLATE)
        return template.render(
            domain_name=domain_name,
            class_name=class_name,
            imports=sorted(imports),
            method_implementations=method_implementations
        ).strip()

    def generate_events_service(self, domain: dict) -> str:
        domain_name = domain['domain']
        self.event_generator.current_domain = domain_name
        self.event_generator.clear()
        
        events = domain.get('events', [])
        event_implementations = []
        for event in events:
            if not event.get('deprecated', False):
                code = self.event_generator.generate_event_implementation(event)
                event_implementations.append(code)

        imports = self.event_generator.imports.copy()
        imports.update(self.event_generator.type_checking_imports)
        imports.add("from .types import *")
        imports.add("from ..types import *")
        imports.add("from typing import Optional, Dict, Any, Callable, TYPE_CHECKING")

        class_name = f"{domain_name}Events"
        template = self.env.from_string(EVENTS_SERVICE_TEMPLATE)
        return template.render(
            domain_name=domain_name,
            class_name=class_name,
            imports=sorted(imports),
            event_implementations=event_implementations
        ).strip()

    def generate_domain_service(self, domain: dict) -> str:
        domain_name = domain['domain']
        domain_description = domain.get('description', f'Access the {domain_name} domain.')
        template = self.env.from_string(DOMAIN_SERVICE_TEMPLATE)
        return template.render(domain_name=domain_name, domain_description=domain_description).strip()
