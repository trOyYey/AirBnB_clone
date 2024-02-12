#!/usr/bin/python3
""" Unittesting Review Class attributes"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class testReview(unittest.TestCase):
    """
    Unittesting Review methods
    """
    def setUp(self):
        """setter of Review"""
        self.review = Review()

    def tearDown(self):
        """ deleting review"""
        del self.review

    def test_inheritance(self):
        """unittest : Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """ testing attributes """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def testDefaultValues(self):
        """ test default values"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def testNoneEmptyAttributes(self):
        """ test non empty attributes"""
        self.review.place_id = "Place_1"
        self.assertEqual(self.review.place_id, "Place_1")

        self.review.user_id = "User_1"
        self.assertEqual(self.review.user_id, "User_1")

        self.review.text = "This is a review"
        self.assertEqual(self.review.text, "This is a review")

    def test_invalid_types(self):
        """test invalid types"""
        self.review.place_id = 11
        self.review.user_id = 11
        self.review.text = 11
        self.assertEqual(self.review.place_id, 11)
        self.assertEqual(self.review.user_id, 11)
        self.assertEqual(self.review.text, 11)

if __name__ == "__main__":
    unittest.main()
