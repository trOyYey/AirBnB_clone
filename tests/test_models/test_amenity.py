#!/usr/bin/python3
""" Unittestng Amenity Class attributes"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class testAmenity(unittest.TestCase):
    """
    Unittesting Amenity methods
    """
    def setUp(self):
        """setter of Amenity"""
        self.amenity = Amenity()

    def tearDown(self):
        """ deleting amenity"""
        del self.amenity

    def test_inheritance(self):
        """unittest : Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """ testing attributes """
        self.assertTrue(hasattr(self.amenity, "name"))

    def testDefaultValues(self):
        """ test default calues"""
        self.assertEqual(self.amenity.name, "")

    def testEmptyAttributes(self):
        """ test empty attributes"""
        self.amenity.name = ""
        self.assertEqual(self.amenity.name, "")

    def testNoneEmptyAttributes(self):
        """ test non empty attributes"""
        self.amenity.name = "Soufiane_Ali"
        self.assertEqual(self.amenity.name, "Soufiane_Ali")

    def test_invalid_types(self):
        """test invalide types"""
        self.amenity.name = 11
        self.assertEqual(self.amenity.name, 11)

if __name__ == "__main__":
    unittest.main()
