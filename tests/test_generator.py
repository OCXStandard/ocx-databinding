#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from ocx_databinding import generator


def test_generate(shared_datadir):
    source = shared_datadir / "unitsmlSchema_lite.xsd"
    package = "unitsml"
    version = "0.9.18"
    result = generator.call_xsdata(
        source=str(source.resolve()),
        package_name=package,
        version=version,
        recursive=True,
    )
    assert result is True
