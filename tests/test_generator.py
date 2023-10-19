#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from ocx_databinding import generator
from ocx_databinding.cli import CONFIG_FILE


def test_generate(shared_datadir):
    source = shared_datadir / "unitsmlSchema_lite.xsd"
    package = "unitsml"
    version = "0.9.18"
    result = generator.generate(str(source.resolve()), package, version, CONFIG_FILE)
    assert result is True
