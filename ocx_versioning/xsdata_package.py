#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update the xsdata package name from the schema version."""
# System imports
from pathlib import Path
import sys
# Third party packages
import packaging.version
from packaging.version import Version, parse
from xsdata.models.config import GeneratorConfig

CONFIG_FILE = 'xsdata.xml'

# The new package version


def usage():
    """Print the usage message and exit"""
    print('Usage: ocx_versioning "module_name" "version_string"\n')


def insert_package_name():
    """ Update the package name in xsdata.xml, see  https://xsdata.readthedocs.io/en/latest/
        If the config file xsdata.xml does not exist, it will be created with the following values set:



        Arguments:
            package: name of package
            new_version: The new version string

    Example:

           > python -m ocx_version ocx 1.0.0
            Updating the configuration file xsdata.xml in module ocx
            New package name is ocx_100 with version: 1.0.0

    """
    if len(sys.argv) == 3:
        new_version = sys.argv[2]
        package = sys.argv[1]
    else:
        usage()
        exit(0)
    # parse new_version
    try:
        v= parse(new_version)
        if v.is_prerelease:
            pr1, pr2 = v.pre
            package_dir = f'{package}_{v.major}{v.minor}{v.micro}{pr1}{pr2}'
        else:
            package_dir = f'{package}_{v.major}{v.minor}{v.micro}'
        file_path = Path(CONFIG_FILE)
        if file_path.exists():
            config = GeneratorConfig.read(file_path)
            print(f'Updating the configuration file {CONFIG_FILE} in module {package}')
        else:
            print(f'Initializing configuration file {CONFIG_FILE}')
            config = GeneratorConfig.create()
        # OCX databindings defaults
        config.output.docstring_style = 'Google'
        # The package name
        config.output.package = package_dir
        config.output.structure_style = 'single-package'
        print(f'New package name is {package_dir} with version: {new_version}')
        with file_path.open("w") as fp:
            config.write(fp, config)
    except packaging.version.InvalidVersion as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    insert_package_name()
