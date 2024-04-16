#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""For testing"""
import sys
from typing import Any
from loguru import logger

from ocx_databinding.cli import generator

config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": str.join(__name__, "log"), "serialize": False},
    ],
}


def main(**kwargs: Any):
    kwargs = {
        # "source": "https://3docx.org/fileadmin/ocx_schema/unitsml/unitsmlSchema_lite-0.9.18.xsd",
        "source": "https://3docx.org/fileadmin//ocx_schema//V300b7//OCX_Schema.xsd",
        "package": "ocx",
        "version": "3.0.0rc7",
        "print": False,
        "recursive": False,
        "slots": False,
    }
    try:
        source = kwargs.pop("source")
        package = kwargs.pop("package")
        stdout = kwargs.pop("print")
        recursive = kwargs.pop("recursive")
        version = kwargs.pop("version")
        slots = kwargs.pop("slots")
        generator.call_xsdata(
            source=source,
            package_name=package,
            version=version,
            stdout=stdout,
            recursive=recursive,
            slots=slots,
        )
    except KeyError as e:
        print(f"Missing option: {e}")


if __name__ == "__main__":
    logger.enable("ocx_databinding")
    main()
