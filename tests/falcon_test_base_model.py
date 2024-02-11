#!/usr/bin/python3
"""testing"""


import unittest
import models
from models.base_model import BaseModel
import os
import models


class TestBaseModel(unittest.TestCase):
    """ Unittest of base_model code"""

    def test_is_an_instance(self):
        """ is a BaseModelInstance an instance of
        BaseModel"""

        BaseModel_I = BaseModel()
        self.assertIsInstance(BaseModel_I, BaseModel)

    def test_docs(self):
        """ everything is documented """

        self.assertIsNotNone(models.base_model.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_different_id(self):
        """ Are BaseModel instances has unque id"""
        i_1 = BaseModel()
        i_2 = BaseModel()
        self.assertNotEqual(i_1, i_2)

    def test_exec_permissions(self):
        """ the Execution permission """

        read = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(read)
        write = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(write)
        exe = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(exe)


if __name__ == "__main__":
    unittest.main()
