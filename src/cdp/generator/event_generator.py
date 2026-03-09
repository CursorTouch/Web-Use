from jinja2 import Environment
from jinja2_strcase import StrcaseExtension
import inflection

EVENT_SERVICES_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Events\"\"\"
from __future__ import annotations
from typing import TypedDict, Optional, Callable, TYPE_CHECKING
from .service import Client
from .events.types import *

if TYPE_CHECKING:
    from ....service import Client

class {{ domain_name }}Events:
    {% if event_implementations | length > 0 %}
    def __init__(self, client: Client):
        self.client = client
    {% for implementation in event_implementations %}
    {{ implementation | indent(4) }}
    {% endfor %}
    {% else %}
    pass
    {% endif %}     
"""

EVENT_IMPLEMENTATION_TEMPLATE = """\
def on_{{ event_name | to_snake }}(self, callback: Callable[[{{ event_name }}Event, str | None], None] | None = None) -> None:
    \"\"\"
    {% if event_description %}{{ event_description | replace("\\n", " ") }}{% else %}No description available for {{ event_name }}.{% endif %}
    
    Args:
        callback (callable, optional): Function called when the event is fired. 
            The callback receives (params: {{ event_name }}Event, session_id: str | None).
    \"\"\"
    self.client.on('{{ domain_name }}.{{ event_name }}', callback)
"""

EVENT_TYPES_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Events\"\"\"
from __future__ import annotations
{% for import_ in imports %}
{{ import_ }}
{% endfor %}
{% if type_checking_imports %}

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    {% for type_checking_import in type_checking_imports %}
    {{ type_checking_import }}
    {% endfor %}
{% endif %}

{% for definition in event_definitions_code %}
{{ definition }}
{% endfor %}         
"""

EVENT_DEFINITION_TEMPLATE = """\
class {{event_name}}Event(TypedDict, total={{total}}):
    {% if not required_parameters and not optional_parameters %}
    pass
    {% else %}
    {% if required_parameters %}
    {% for parameter in required_parameters %}
    {{ parameter['name'] }}: {{ parameter['type'] }}
    {% if parameter['description'] %}
    \"\"\"{{ parameter['description'] | replace('\\n', ' ') | replace('`', '') }}\"\"\"
    {% endif %}
    {% endfor %}
    {% endif %}
    {% if optional_parameters %}
    {% for parameter in optional_parameters %}
    {{ parameter['name'] }}: NotRequired[{{ parameter['type'] }}]
    {% if parameter['description'] %}
    \"\"\"{{ parameter['description'] | replace('\\n', ' ') | replace('`', '') }}\"\"\"
    {% endif %}
    {% endfor %}
    {% endif %}
    {% endif %}
"""

class EventGenerator:
    def __init__(self,path, protocol_package:str):
        self.path = path
        self.protocol_package = protocol_package
        self.current_domain:str=None
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])
        self.imports = set()
        self.generated_events = set()
        self.type_checking_imports = set()

    def clear(self):
        self.imports.clear()
        self.generated_events.clear()
        self.type_checking_imports.clear()

    def generate_event_services(self,domain:dict):
        self.current_domain=domain.get('domain')
        events=domain.get('events',[])
        event_implementations=[self.generate_event_implementation(event) for event in events]
        template = self.env.from_string(EVENT_SERVICES_TEMPLATE)
        code = template.render(
            domain_name=self.current_domain,
            event_implementations=event_implementations,
        )
        return code.strip()

    def generate_event_implementation(self,event:dict):
        event_name=event.get('name')
        event_description=event.get('description','')
        template = self.env.from_string(EVENT_IMPLEMENTATION_TEMPLATE)
        code = template.render(
            event_name=event_name,
            domain_name=self.current_domain,
            event_description=event_description
        )
        return code.strip()

    def generate_event_types(self,domain:dict):
        self.current_domain=domain.get('domain')
        events=domain.get('events',[])
        self.clear()
        self.imports.add("from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple")
        for event in events:
            self.generated_events.add(event.get('name'))

        event_definitions_code=[self.generate_event_definition(event) for event in events if not event.get('deprecated',False)]
        template = self.env.from_string(EVENT_TYPES_TEMPLATE)
        code = template.render(
            domain_name=self.current_domain,
            event_definitions_code=event_definitions_code,
            imports=sorted(filter(lambda x: not x.startswith(f'from {self.protocol_package}.{self.current_domain}.types import'),self.imports)),
            type_checking_imports=sorted(self.type_checking_imports),
        )
        return code.strip()

    def generate_event_definition(self,event_definition): 
        event_name=event_definition.get('name')   
        parameters=event_definition.get('parameters',[])
        required_parameters=[]
        optional_parameters=[]
        for parameter in parameters:
            parameter['type'] = self.resolve_parameter_type(parameter)
            if parameter.get('optional',False):
                optional_parameters.append(parameter)
            else:
                required_parameters.append(parameter)

        total = not (optional_parameters and not required_parameters)
        template = self.env.from_string(EVENT_DEFINITION_TEMPLATE)
        code = template.render(
            total=total,
            event_name=event_name,
            required_parameters=required_parameters,
            optional_parameters=optional_parameters,
        )
        self.generated_events.add(event_name)
        return code.strip()

    def resolve_parameter_type(self, parameter:dict):
        if "$ref" in parameter:
            return self.resolve_type_reference(parameter)
        parameter_type=parameter.get("type","any")
        match parameter_type:
            case 'object':
                return "Dict[str, Any]"
            case 'array':
                items=parameter.get('items',{})
                return f"List[{self.resolve_type_reference(items) if '$ref' in items else self.map_primitive_type(items.get('type'))}]"
            case 'string':
                if 'enum' in parameter:
                    return f"Literal[{', '.join(f'\"{v}\"' for v in parameter.get('enum'))}]"
                else:
                    return "str"
            case _:
                return self.map_primitive_type(parameter_type)

    def resolve_type_reference(self, type_ref:dict):
        ref=type_ref.get('$ref')
        if '.' in ref:
            parts=ref.split('.')
            type_name=parts[1]
            domain=inflection.underscore(parts[0])
            self.type_checking_imports.add(f"from {self.protocol_package}.{domain}.types import {type_name}")
            return type_name
        else:
            domain=inflection.underscore(self.current_domain)
            self.type_checking_imports.add(f"from {self.protocol_package}.{domain}.types import {ref}")
            return ref

    def map_primitive_type(self, type_name: str):
        match type_name:
            case "string":
                return "str"
            case "object":
                return "Dict[str, Any]"
            case "number":
                return "float"
            case "integer":
                return "int"
            case "boolean":
                return "bool"
            case _:
                return "Any"