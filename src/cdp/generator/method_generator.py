from jinja2_strcase import StrcaseExtension
from jinja2 import Environment
import inflection

METHOD_IMPLEMENTATION_TEMPLATE = """\
async def {{ method_name | to_snake }}(self, params: {{ method_name }}Parameters | None = None, session_id: str | None = None) -> {% if return_parameters|length > 0 %}{{ method_name }}Returns{% else %}Dict[str, Any]{% endif %}:
    \"\"\"
    {% if method_description %}{{ method_description | replace("\\n", " ") }}{% else %}No description available for {{ method_name }}.{% endif %}
    
    Args:
        params ({{ method_name }}Parameters, optional): Parameters for the {{ method_name }} method.
        session_id (str, optional): Target session ID for flat protocol usage.
        
    Returns:
        {% if return_parameters|length > 0 %}{{ method_name }}Returns{% else %}Dict[str, Any]{% endif %}: The result of the {{ method_name }} call.
    \"\"\"
    return await self.client.send(method="{{ domain_name }}.{{ method_name }}", params=params, session_id=session_id)
"""

METHOD_TYPES_TEMPLATE = """\
\"\"\"CDP {{ domain_name }} Methods Types\"\"\"
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

{% for definition in parameter_definitions_code %}
{{ definition }}
{% endfor %}
{% for definition in return_definitions_code %}
{{ definition }}
{% endfor %}
"""

PARAMETER_DEFINITION_TEMPLATE = """\
class {{ method_name }}Parameters(TypedDict, total={{ total }}):
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

RETURN_DEFINITION_TEMPLATE = """\
class {{ method_name }}Returns(TypedDict):
    {% if not return_parameters %}
    pass
    {% else %}
    {% for return_parameter in return_parameters %}
    {{ return_parameter['name'] }}: {{ return_parameter['type'] }}
    {% if return_parameter['description'] %}
    \"\"\"{{ return_parameter['description'] | replace('\\n', ' ') | replace('`', '') }}\"\"\"
    {% endif %}
    {% endfor %}
    {% endif %}
"""

class MethodGenerator:
    def __init__(self,path, protocol_package:str):
        self.path = path
        self.protocol_package = protocol_package
        self.current_domain:str=None
        self.env=Environment(trim_blocks=True,lstrip_blocks=True,extensions=[StrcaseExtension])
        self.imports = set()
        self.generated_methods = set()
        self.type_checking_imports = set()

    def clear(self):
        self.imports.clear()
        self.generated_methods.clear()
        self.type_checking_imports.clear()

    def generate_method_implementation(self,method:dict):
        method_name=method.get('name')
        method_description=method.get('description','')
        parameters=method.get('parameters',[])
        return_parameters=method.get('returns',[])
        template = self.env.from_string(METHOD_IMPLEMENTATION_TEMPLATE)
        code = template.render(
            domain_name=self.current_domain,
            method_name=method_name,
            method_description=method_description,
            parameters=parameters,
            return_parameters=return_parameters,
        )
        return code.strip()

    def generate_method_types(self,domain:dict):
        self.current_domain=domain.get('domain')
        methods=domain.get('commands',[])
        self.clear()
        self.imports.add("from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple")
        for method in methods:
            self.generated_methods.add(method.get('name'))

        parameter_definitions_code=[self.generate_parameter_definition(method) for method in methods if not method.get('deprecated',False)]
        return_definitions_code=[self.generate_return_definition(method) for method in methods if not method.get('deprecated',False)]

        template = self.env.from_string(METHOD_TYPES_TEMPLATE)
        code = template.render(
            domain_name=self.current_domain,
            parameter_definitions_code=parameter_definitions_code,
            return_definitions_code=return_definitions_code,
            imports=sorted(filter(lambda x: not x.startswith(f'from {self.protocol_package}.{self.current_domain}.types import'),self.imports)),
            type_checking_imports=sorted(self.type_checking_imports),
        )
        return code.strip()
    
    def generate_parameter_definition(self, method_definition:dict):
        method_name=method_definition.get('name')
        parameters=method_definition.get('parameters',[])
        if not parameters:
            return ''
        required_parameters=[]
        optional_parameters=[]
        for parameter in parameters:
            parameter['type'] = self.resolve_parameter_type(parameter)
            if parameter.get('optional',False):
                optional_parameters.append(parameter)
            else:
                required_parameters.append(parameter)
        total = not (optional_parameters and not required_parameters)
        template = self.env.from_string(PARAMETER_DEFINITION_TEMPLATE)
        code = template.render(
            total=total,
            method_name=method_name,
            required_parameters=required_parameters,
            optional_parameters=optional_parameters,
        )
        self.generated_methods.add(method_name)
        return code.strip()

    def generate_return_definition(self, method_definition:dict):
        method_name=method_definition.get('name')
        return_parameters=method_definition.get('returns',[])
        if not return_parameters:
            return ""
        for return_parameter in return_parameters:
            return_parameter['type']=self.resolve_parameter_type(return_parameter)
        template = self.env.from_string(RETURN_DEFINITION_TEMPLATE)
        code = template.render(
            method_name=method_name,
            return_parameters=return_parameters
        )
        self.generated_methods.add(method_name)
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