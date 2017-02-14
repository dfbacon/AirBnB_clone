#!/usr/bin/python3
'''
This is the 'test_place' module.

test_amenity uses unittest to test the 'models/place' module.
All credit for this module goes to Danton Rodriguez
(https://github.com/p0516357)
'''
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Test for Place class
    """
    def setUp(self):
        """sets up objects for testing later
        """
        self.test_model1 = Place()
        self.test_model2 = Place()

    def test_basic_setup(self):
        """test for Place class attributes
        """
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(hasattr(self.test_model1, "city_id"))
        self.assertTrue(hasattr(self.test_model2, "user_id"))
        self.assertTrue(hasattr(self.test_model1, "number_rooms"))
        self.assertTrue(hasattr(self.test_model1, "number_bathrooms"))
        self.assertTrue(hasattr(self.test_model2, "latitude"))
        self.assertTrue(hasattr(self.test_model1, "amenities"))
        self.assertTrue(hasattr(self.test_model1, "latitude"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)

    def test_types(self):
        """tests whether isntance attribute types are correct
        """
        self.assertTrue(type(self.test_model1.amenities) is str)
        self.assertTrue(type(self.test_model1.name) is str)
        self.assertTrue(type(self.test_model1.city_id) is str)
        self.assertTrue(type(self.test_model1.user_id) is str)
        self.assertTrue(type(self.test_model1.description) is str)
        self.assertTrue(type(self.test_model1.number_rooms) is int)
        self.assertTrue(type(self.test_model1.number_bathrooms) is int)
        self.assertTrue(type(self.test_model1.max_guest) is int)
        self.assertTrue(type(self.test_model1.price_by_night) is int)
        self.assertTrue(type(self.test_model1.longitude) is float)
        self.assertTrue(type(self.test_model1.latitude) is float)

    def test_save(self):
        """testing whether save updates the updated_at attribute
        """
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
