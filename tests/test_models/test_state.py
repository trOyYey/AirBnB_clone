#!/usr/bin/python3
""" Unittesting State Class attributes"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """
    Unittesting State methods
    """
    def setUp(self):
        """setter of State"""
        self.state = State()

    def tearDown(self):
        """ deleting state"""
        del self.state

    def test_inheritance(self):
        """unittest : State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """ testing attributes """
        self.assertTrue(hasattr(self.state, "name"))

    def testDefaultValues(self):
        """ test default values"""
        self.assertEqual(self.state.name, "")

    def testNoneEmptyAttributes(self):
        """ test non empty attributes"""
        self.state.name = "State_1"
        self.assertEqual(self.state.name, "State_1")

    def test_invalid_types(self):
        """test invalid types"""
        self.state.name = 11
        self.assertEqual(self.state.name, 11)


if __name__ == "__main__":
    unittest.main()
