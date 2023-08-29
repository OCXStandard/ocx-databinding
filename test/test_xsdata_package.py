#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

from unittest import TestCase
from typing import Optional
from urllib.request import urlopen
from ocx_versioning.xsdata_package import insert_package_name

class Test(TestCase):

    def load_resource(self, uri: str) -> Optional[bytes]:
        """Read and return the contents of the given uri."""
        try:
             return urlopen(uri).read()  # nosec
        except OSError:
            print("Resource not found %s", uri)


    def test_insert_package_name(self,package: str = 'ocx', version:str = '1.0.0'):

        insert_package_name()
        self.fail()
