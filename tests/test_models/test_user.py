#!/usr/bin/python3
""" Unittestng User Class attributes"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """
    Unittesting user methods
    """

    def settingup(self):
        """
        setter for user
        """
        self.user = User()

    def tearDown(self):
        """
        deleting user
        """
        del self.user

    def test_inheritance(self):
        """
        unittest user inheritance method
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        testing attributes
        """
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_values(self):
        """
        test default values
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """
        testing string represantation
        """
        exp = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), exp)

    def test_to_dict_method(self):
        """
        testing to_dict method
        """
        exp = {
            'id': self.user.id,
            'created_at': self.user.created_at.isoformat(),
            'updated_at': self.user.updated_at.isoformat(),
            '__class__': 'User'
        }
        self.assertEqual(self.user.to_dict(), exp)

    def test_empty_attributes(self):
        """
        testing empty attributes
        """
        self.user.email = ""
        self.user.password = ""
        self.user.first_name = ""
        self.user.last_name = ""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_non_empty_attributes(self):
        """
        testing non empty attributes
        """
        self.user.email = "spody@salem.com"
        self.user.password = "123123123"
        self.user.first_name = "salem"
        self.user.last_name = "baskal"
        self.assertEqual(self.user.email, "spody@salem.com")
        self.assertEqual(self.user.password, "123123123")
        self.assertEqual(self.user.first_name, "salem")
        self.assertEqual(self.user.last_name, "baskal")

    def test_invalid_types(self):
        """
        test_invalid_types
        """
        self.user.email = 332
        self.user.password = 332
        self.user.first_name = 332
        self.user.last_name = 332
        self.assertEqual(self.user.email, 332)
        self.assertEqual(self.user.password, 332)
        self.assertEqual(self.user.first_name, 332)
        self.assertEqual(self.user.last_name, 332)


if __name__ == '__main__':
    unittest.main()
