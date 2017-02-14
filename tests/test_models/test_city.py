#!/usr/bin/python3
'''
This is the 'test_city' module.

test_city uses unittest to test the 'models/city' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Test for City class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = City()
        self.test_model2 = City()

    def test_basic_setup(self):
        """test for init of class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "state_id"))
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)

    def test_types(self):
        """testing for proper typing of city attributes
        """
        self.assertTrue(type(self.test_model1.state_id) is str)
        self.assertTrue(type(self.test_model1.name) is str)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
