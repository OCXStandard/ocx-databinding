#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from typer.testing import CliRunner
from ocx_databinding.cli import databinding
from ocx_databinding import __version__
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
    package = "unitsml"
    version = "0.9.18"
    result = runner.invoke(
        databinding, ["generate", str(source.resolve()), package, version]
    )
    assert result.exit_code == 0


def test_generate_from_url():
    runner = CliRunner()
    source = SCHEMA_URL
    package = "ocx"
    version = "3.0.0"
    result = runner.invoke(databinding, ["generate", source, package, version])
    assert result.exit_code == 0
