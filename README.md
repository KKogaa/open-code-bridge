# Open Code Bridge
The Open Code Bridge is a tool that generates code for various programming languages from an OpenAPI specification.
This tool aims to bridge the gap between API definition and code implementation. Enabling developers to create for example
Typescript types, Python classes, and Go structs based on the provided OpenAPI file.

## Installation
```bash
pip install .
```

## Usage
```
usage: ocb [-h] [--language {python,go,typescript}] [--output OUTPUT] [openapi]

Open Code Bridge

positional arguments:
  openapi               The location of the OpenAPI specification file.

options:
  -h, --help            show this help message and exit
  --language {python,go,typescript}
                        The target language for code generation: python, go, or typescript.
  --output OUTPUT       The output location where the generated code will be saved.

```


```bash
ocb OPENAPISPEC --language python --output NAME
```

For example the following spec:

will generate the following code:

