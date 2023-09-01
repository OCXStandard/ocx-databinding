#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script entry point."""
# System imports
from __future__ import annotations
# Third party
import typer
from typing_extensions import Annotated

# Project
from ocx_versioning import __app_name__, __version__
from ocx_versioning import generator

databinding = typer.Typer()

CONFIG_FILE = 'xsdata.xml'

# The new package version


@databinding.command()
def generate(
    source: Annotated[
    str, typer.Argument(
    help=' The input source can be either a filepath, uri or a directory containing xml, json, xsd and wsdl files.')],
    package: Annotated[str, typer.Argument(help='The name of the databinding destination folder')],
    version: Annotated[str, typer.Argument(help='The source schema version number.')],
    config: Annotated[str, typer.Option(help='The generator config file', prompt=True)] = CONFIG_FILE,
    stdout: Annotated[bool, typer.Option(help='Print the output to the console.')] = False,
    recursive: Annotated[bool,
    typer.Option(help='Search files recursively in the source directory', prompt=True)] = False

):
    """Generate code from xml schemas, webservice definitions and any xml or json document.
       The input source can be either a filepath, uri or a directory containing  xml, json, xsd and wsdl files
    """
    result = generator.generate(source, package, version, config, stdout, recursive)



@databinding.command()
def version():
    """Print the version number and exit."""
    print(__version__)