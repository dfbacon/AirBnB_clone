#!/usr/bin/python3
'''
This is the 'test_state' module.

test_state uses unittest to test the 'models/state' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Test for State class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = State()
        self.test_model2 = State()

    def test_basic_setup(self):
        """test for proper init of State class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertFalse(hasattr(self.test_model1, "first_name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
        self.assertTrue(type(m1c) is datetime.datetime)

    def test_types(self):
        """testing types of class attributes
        """
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
