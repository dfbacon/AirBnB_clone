#!/usr/bin/python3
'''
This is the 'test_file_storage' module.

test_file_storage uses unittest to test the 'models/engine/file_storage' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test Class for FileStorage Class
    """
    def setUp(self):
        """setup method for FileStorage test class
        """
        self.storage = FileStorage()

    def test_attrs(self):
        """test for presence of attributes
        """
        self.assertFalse(hasattr(self.storage, "milkyway.json"))

if "__main__" == __name__:
    unittest.main()
