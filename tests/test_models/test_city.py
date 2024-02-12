#!/usr/bin/python3
""" Unittesting City Class attributes"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """
    Unittesting City methods
    """
    def setUp(self):
        """setter of City"""
        self.city = City()

    def tearDown(self):
        """ deleting city"""
        del self.city

    def test_inheritance(self):
        """unittest : City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """ testing attributes """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def testDefaultValues(self):
        """ test default values"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def testNoneEmptyAttributes(self):
        """ test non empty attributes"""
        self.city.state_id = "State_1"
        self.assertEqual(self.city.state_id, "State_1")

        self.city.name = "City_1"
        self.assertEqual(self.city.name, "City_1")

    def test_invalid_types(self):
        """test invalid types"""
        with self.assertRaises(TypeError):
            self.city.state_id = 11
            self.city.name = 11

if __name__ == "__main__":
    unittest.main()
