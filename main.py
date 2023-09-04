#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""For testing"""
import sys
from typing import Any
from loguru import logger

from  ocx_generator.cli import generator

config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": str.join(__name__, "log"), "serialize": True},
    ],
}


def main(**kwargs: Any):
    kwargs =  {'source': 'tests/data/unitsMLSchema_lite.xsd',
    'destination': 'tests/data',
    'package': 'unitsml',
    'print': False,
    'recursive': False,
    'config': 'xsdata.xml',
    'version': '0.9.18'
    }
    try:
        source = kwargs.pop("source")
        package = kwargs.pop("package")
        stdout = kwargs.pop("print")
        recursive = kwargs.pop("recursive")
        config = kwargs.pop("config")
        version = kwargs.pop("version")
        generator.generate(source, package, version, config, stdout, recursive)
    except KeyError as e:
        print(f'Missing option: {e}')


if __name__ == "__main__":
    logger.enable('ocx_generator')
    main()