from typing import List


class Property:
    name: str
    type: str

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return f"{self.name}: {self.type}"


class Schema:
    name: str
    method: str
    type: str
    properties: List[Property]
    message_type: str

    def __init__(
        self,
        type: str,
        properties: dict,
        method: str,
        name: str,
        message_type: str,
    ):
        self.type = type
        self.properties = [
            Property(name=key, type=val["type"])
            for key, val in properties.items()
        ]
        self.method = method
        self.name = name[1:]
        self.message_type = message_type

    def get_schema_full_name(self) -> str:
        return f"{self.method}{self.name}{self.message_type}"

    def __str__(self) -> str:
        printed_props = [str(property) for property in self.properties]
        printed_props = " ".join(printed_props)
        return f"SCHEMA name: {self.name} method: {self.method} type: {self.type} properties: {printed_props}"
