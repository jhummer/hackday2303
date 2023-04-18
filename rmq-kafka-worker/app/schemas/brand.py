from dataclasses import dataclass, asdict, fields
from typing import Optional


@dataclass
class Brand:
    id: int
    name: str


json_schema = {
    "namespace": "vehicle",
    "type": "record",
    "name": Brand.__name__,
    "fields": [],
}

type_map = {
    str: "string",
    int: "int"
}

for field in fields(Brand):
    if field.type in [str, int]:
        if field.default is None:
            json_schema["fields"].append({"name": field.name, "type": ["null", type_map[field.type]]})
        else:
            json_schema["fields"].append({"name": field.name, "type": type_map[field.type]})
