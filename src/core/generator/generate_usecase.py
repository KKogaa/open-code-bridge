from typing import List

from core.generator.schema import Schema
from yaml import load, Loader
from pprint import pprint


class Generator:
    def __init__(
        self, language: str, open_api_location: str, output_location: str
    ):
        self.language = language
        self.open_api_location = open_api_location
        self.output_location = output_location

    # repository
    def load_openapi_file(self) -> List[Schema]:

        stream = open("./src/samples/chatgpt.yaml", "r")
        data = load(stream, Loader=Loader)
        schemas = []

        # TODO: mega refactor
        for path, path_content in data["paths"].items():
            for method, method_content in path_content.items():

                if method_content.get("requestBody"):
                    type = method_content["requestBody"]["content"][
                        "application/json"
                    ]["schema"]["type"]
                    properties = method_content["requestBody"]["content"][
                        "application/json"
                    ]["schema"]["properties"]
                    # ENUM for message_type
                    schemas.append(
                        Schema(
                            type=type,
                            properties=properties,
                            method=method,
                            name=path,
                            message_type="request",
                        )
                    )

                if method_content.get("responses"):
                    v = method_content.get("responses")

                    if v.get("200"):
                        type = v["200"]["content"]["application/json"][
                            "schema"
                        ]["type"]
                        # WARNING if type array has items else it doesnt
                        properties = v["200"]["content"]["application/json"][
                            "schema"
                        ]["items"]["properties"]
                        schemas.append(
                            Schema(
                                type=type,
                                properties=properties,
                                method=method,
                                name=path,
                                message_type="response",
                            )
                        )

                    if v.get("201"):
                        type = v["201"]["content"]["application/json"][
                            "schema"
                        ]["type"]
                        properties = v["201"]["content"]["application/json"][
                            "schema"
                        ]["properties"]
                        schemas.append(
                            Schema(
                                type=type,
                                properties=properties,
                                method=method,
                                name=path,
                                message_type="response",
                            )
                        )

                # just use 200 or 201
        return schemas

    def output_typescript(self, schemas: List[Schema]) -> List[str]:

        for schema in schemas:
            # make method in schema
            head = f"export interface {schema.get_schema_full_name()} {{\n"

            body = ""
            for property in schema.properties:
                body += f"  {str(property)}\n"

            tail = '}'

            print(head + body + tail)

        return []

    def execute(self):
        # TODO: find and parse openapi spec
        schemas: List[Schema] = self.load_openapi_file()

        print(self.output_typescript(schemas))

