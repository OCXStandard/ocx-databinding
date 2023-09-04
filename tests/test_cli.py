#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from typer.testing import CliRunner
from ocx_generator.cli import databinding
from ocx_generator import __version__

def test_version():
    """Test ouput of cli version."""
    runner = CliRunner()
    result = runner.invoke(databinding, ['version'])
    assert str(result.output).find(__version__) != -1

def test_help():
    """Test help output."""
    runner = CliRunner()
    result = runner.invoke(databinding, ['generate', '--help'])
    assert result.exit_code ==0

def test_generate(shared_datadir):

    runner = CliRunner()
    source = shared_datadir / 'unitsmlSchema_lite.xsd'
    package = 'unitsml'
    version = '0.9.18'
    result = runner.invoke(databinding, ['generate', str(source.resolve()), package, version])
    assert result.exit_code ==0

