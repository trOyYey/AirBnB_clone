#!/usr/bin/python3
""" Unittesting Place Class attributes"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testPlace(unittest.TestCase):
    """
    Unittesting Place methods
    """
    def setUp(self):
        """setter of Place"""
        self.place = Place()

    def tearDown(self):
        """ deleting place"""
        del self.place

    def test_inheritance(self):
        """unittest : Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """ testing attributes """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def testDefaultValues(self):
        """ test default values"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        
    def testNoneEmptyAttributes(self):
        """ test non empty attributes"""
        self.place.name = "Soufiane_Ali"
        self.assertEqual(self.place.name, "Soufiane_Ali")

        self.place.city_id = "City_1"
        self.assertEqual(self.place.city_id, "City_1")

        self.place.user_id = "User_1"
        self.assertEqual(self.place.user_id, "User_1")

        self.place.description = "A beautiful place"
        self.assertEqual(self.place.description, "A beautiful place")

        self.place.number_rooms = 3
        self.assertEqual(self.place.number_rooms, 3)

        self.place.number_bathrooms = 2
        self.assertEqual(self.place.number_bathrooms, 2)

        self.place.max_guest = 4
        self.assertEqual(self.place.max_guest, 4)

        self.place.price_by_night = 100
        self.assertEqual(self.place.price_by_night, 100)

        self.place.latitude = 40.7128
        self.assertEqual(self.place.latitude, 40.7128)

        self.place.longitude = -74.0060
        self.assertEqual(self.place.longitude, -74.0060)

        self.place.amenity_ids = ["Amenity_1", "Amenity_2"]
        self.assertEqual(self.place.amenity_ids, ["Amenity_1", "Amenity_2"])


if __name__ == "__main__":
    unittest.main()
