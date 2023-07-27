import argparse
from enum import Enum

from core.generator.generate_usecase import Generator


class OutputLang(Enum):
    PYTHON = "python"
    GO = "go"
    TYPESCRIPT = "typescript"


class Commands(Enum):
    GENERATE = "generate"


def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Open Code Bridge"
    )
    parser.add_argument(
        "openapi",
        type=str,
        nargs="?",
        help="The location of the OpenAPI specification file.",
    )

    parser.add_argument(
        "--language",
        type=str,
        choices=[lang.value for lang in OutputLang],
        help="The target language for code generation: python, go, or typescript.",
    )

    parser.add_argument(
        "--output",
        type=str,
        help="The output location where the generated code will be saved.",
    )
    return parser.parse_args()


def cli():
    args: argparse.Namespace = parse_args()
    if args.openapi:
        generator = Generator(args.language, args.openapi, args.output)
        generator.execute()
