from jinja2 import Environment
from pathlib import Path
import inflection

TYPES_TEMPLATE = """\
\"\"\"CDP {{ current_domain }} Types\"\"\"
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

{% for definition in type_definitions_code %}
{{ definition }}
{% endfor %}
"""

ARRAY_TYPE_TEMPLATE = """\
{{ type_name }} = List[{{ type_type }}]
{% if type_description %}
\"\"\"{{ type_description | replace('\\n', ' ') | replace('`', '') }}\"\"\"
{% endif %}
"""

PRIMITIVE_TYPE_TEMPLATE = """\
{{ type_name }} = {{ type_type }}
{% if type_description %}
\"\"\"{{ type_description | replace('\\n', ' ') | replace('`', '') }}\"\"\"
{% endif %}
"""

LITERAL_TYPE_TEMPLATE = """\
{{ type_name }} = Literal[{{ enum_values }}]
{% if type_description %}
\"\"\"{{ type_description | replace('\\n', ' ') }}\"\"\"
{% endif %}
"""

OBJECT_TYPE_TEMPLATE = """\
class {{ type_name }}(TypedDict, total={{ total }}):
    {% if type_description %}
    \"\"\"{{ type_description | replace('\\n', ' ') | replace('`', '') }}\"\"\"
    {% endif %}
    {% if not required_properties and not optional_properties %}
    pass
    {% else %}
    {% if required_properties %}
    {% for property in required_properties %}
    {{ property['name'] }}: {{ property['type'] }}
    {% if property.get('description') %}
    \"\"\"{{ property['description'] | replace('\\n', ' ') | replace('\\\"', '') | replace('`','') }}\"\"\"
    {% endif %}
    {% endfor %}
    {% endif %}
    {% if optional_properties %}
    {% for property in optional_properties %}
    {{ property['name'] }}: NotRequired[{{ property['type'] }}]
    {% if property.get('description') %}
    \"\"\"{{ property['description'] | replace('\\n', ' ') | replace('`', '') }}\"\"\"
    {% endif %}
    {% endfor %}
    {% endif %}
    {% endif %}
"""

class TypeGenerator:
    def __init__(self,path:Path, protocol_package:str):
        self.path = path
        self.protocol_package = protocol_package
        self.current_domain:str = None
        self.env=Environment(trim_blocks=True,lstrip_blocks=True)
        self.imports = set()
        self.generated_types = set()
        self.type_checking_imports = set()

    def clear(self):
        self.imports.clear()
        self.generated_types.clear()
        self.type_checking_imports.clear()

    def generate_types(self, domain: dict):
        self.current_domain = domain.get('domain')
        type_definitions = domain.get('types', [])
        self.clear()
        self.imports.add("from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple")
        for type_definition in type_definitions:
            self.generated_types.add(type_definition.get('id'))

        type_definitions_code=[self.generate_type_definition(type_definition) for type_definition in type_definitions]
        template = self.env.from_string(TYPES_TEMPLATE)
        code = template.render(
            current_domain=self.current_domain,
            type_definitions_code=type_definitions_code,
            imports=sorted(filter(lambda x: not x.startswith(f'from {self.protocol_package}.{inflection.underscore(self.current_domain)}.types import'),self.imports)),
            type_checking_imports=sorted(self.type_checking_imports),
        )
        return code.strip()

    def generate_type_definition(self, type_definition: dict):
        type_type = type_definition.get('type')
        if type_type == "string" and "enum" in type_definition:
            return self.generate_literal_type(type_definition)
        elif type_type == "object":
            return self.generate_object_type(type_definition)
        elif type_type == "array":
            return self.generate_array_type(type_definition)
        elif type_type in ["string", "number", "integer", "boolean"]:
            return self.generate_primitive_type(type_definition)

    def generate_array_type(self, type_definition: dict):
        type_name = type_definition.get('id')
        type_description = type_definition.get('description')
        items = type_definition.get('items', {})
        template = self.env.from_string(ARRAY_TYPE_TEMPLATE)
        code = template.render(
            type_name=type_name,
            type_type=self.resolve_type_reference(items) if '$ref' in items else self.map_primitive_type(items.get('type')),
            type_description=type_description,
        )
        self.generated_types.add(type_name)
        return code.strip()

    def generate_primitive_type(self, type_definition: dict):
        type_name=type_definition.get('id')
        type_description=type_definition.get('description')
        type_type=type_definition.get('type')
        template = self.env.from_string(PRIMITIVE_TYPE_TEMPLATE)
        code = template.render(
            type_name=type_name,
            type_type=self.map_primitive_type(type_type),
            type_description=type_description,
        )
        self.generated_types.add(type_name)
        return code.strip()

    def generate_literal_type(self, type_definition: dict):
        type_name = type_definition.get('id')
        type_description = type_definition.get('description')
        enum_values = type_definition.get('enum', [])
        template = self.env.from_string(LITERAL_TYPE_TEMPLATE)
        code = template.render(
            type_name=type_name,
            enum_values=",".join(f"'{v}'" for v in enum_values),
            type_description=type_description,
        )
        self.generated_types.add(type_name)
        return code.strip()

    def generate_object_type(self, type_definition: dict):
        type_name = type_definition.get('id')
        type_description = type_definition.get('description', '')
        properties = type_definition.get('properties', [])
        required_properties = []
        optional_properties = []
        for property in properties:
            is_optional = property.get('optional', False)
            if property.get('deprecated', False):
                continue
            property['type'] = self.resolve_property_type(property)
            if is_optional:
                optional_properties.append(property)
            else:
                required_properties.append(property)
        total = not (optional_properties and not required_properties)
        template = self.env.from_string(OBJECT_TYPE_TEMPLATE)
        code = template.render(
            type_name=type_name,
            total=total,
            type_description=type_description,
            required_properties=required_properties,
            optional_properties=optional_properties,
        )
        self.generated_types.add(type_name)
        return code.strip()

    def resolve_property_type(self, property: dict):
        if '$ref' in property:
            return self.resolve_type_reference(property)
        property_type = property.get('type','any')
        match property_type:
            case 'object':
                return "Dict[str, Any]"
            case 'array':
                items=property.get('items',{})
                return f"List[{self.resolve_type_reference(items) if '$ref' in items else self.map_primitive_type(items.get('type'))}]"
            case 'string':
                if 'enum' in property:
                    return f"Literal[{', '.join(f'\"{v}\"' for v in property.get('enum'))}]"
                else:
                    return "str"
            case _:
                return self.map_primitive_type(property_type)
        
    def resolve_type_reference(self, type_ref:dict):
        ref = type_ref.get('$ref')
        if '.' in ref:
            parts=ref.split('.')
            type_name=parts[1]
            current_domain=self.current_domain.lower()
            domain=parts[0].lower()
            if (current_domain!=domain) or (type_name not in self.generated_types):
                domain=inflection.underscore(domain)
                self.type_checking_imports.add(f"from {self.protocol_package}.{domain}.types import {type_name}")
            return type_name
        else:
            if ref not in self.generated_types:
                domain=inflection.underscore(self.current_domain)
                self.imports.add(f"from {self.protocol_package}.{domain}.types import {ref}")
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