#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from pathlib import Path
from packaging.version import parse
import filecmp
import shutil
from typer.testing import CliRunner
from ocx_databinding.cli import databinding
from ocx_databinding import __version__
from ocx_databinding.generator import package_version
from conftest import SCHEMA_URL


def test_version():
    """Test ouput of cli version."""
    runner = CliRunner()
    result = runner.invoke(databinding, ["version"])
    assert __version__ in str(result.output)


def test_help():
    """Test help output."""
    runner = CliRunner()
    result = runner.invoke(databinding, ["generate", "--help"])
    assert result.exit_code == 0


def test_generate_from_file(shared_datadir):
    runner = CliRunner()
    source = shared_datadir / "unitsmlSchema_lite.xsd"
    reference_dir = shared_datadir / "reference"
    package = "unitsml"
    version = "0.9.18"
    v = parse(version)
    package_v = package_version(
        name=package,
        major=v.major,
        minor=v.minor,
        micro=v.micro,
    )
    destination_folder = Path(package) / Path(package_v)

    result = runner.invoke(
        databinding, ["generate", str(source.resolve()), package, version]
    )

    # Check command succeeded
    assert result.exit_code == 0

    # Verify output directory and key files exist
    assert (destination_folder / "__init__.py").exists()

    # Compare with reference files
    reference_dir = Path(__file__).parent / "reference" / f"{package}_{version}"
    assert filecmp.cmpfiles(
        destination_folder, reference_dir, ["__init__.py"], shallow=False
    )

    # Clean up by removing generated files
    shutil.rmtree(destination_folder.resolve())


def test_generate_from_url():
    runner = CliRunner()
    source = SCHEMA_URL
    package = "ocx"
    version = "3.0.0"
    result = runner.invoke(databinding, ["generate", source, package, version])
    assert result.exit_code == 0
