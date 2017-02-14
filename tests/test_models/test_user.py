#!/usr/bin/python3
'''
This is the 'test_user' module.

test_user uses unittest to test the 'models/user' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Test for User class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = User()
        self.test_model2 = User()

    def test_basic_setup(self):
        """test for proper instantiation of user class
        """
        self.assertTrue(hasattr(self.test_model1, "last_name"))
        self.assertTrue(hasattr(self.test_model1, "first_name"))
        self.assertTrue(hasattr(self.test_model1, "email"))
        self.assertTrue(hasattr(self.test_model1, "password"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """checking proper types for user class attributes
        """
        self.assertTrue(type(self.test_model1.last_name) is str)
        self.assertTrue(type(self.test_model1.first_name) is str)
        self.assertTrue(type(self.test_model1.email) is str)
        self.assertTrue(type(self.test_model1.password) is str)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
