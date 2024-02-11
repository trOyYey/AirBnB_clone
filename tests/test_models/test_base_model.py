#!/usr/bin/python3
import unittest
import models.base_model
from models.base_model import BaseModel
import os
import models

class TestBaseModel(unittest.TetCase):
    """ Unittest of base_model code"""

    def test_is_an_instance(self):
        """ is a BaseModelInstance an instance of
        BaseModel"""

        BaseModel_I = BaseModel()
        self.assertIsInstance(BaseModel_I, BaseModel)

    def test_docs(self):
        """ all = (moduls, class, methodes) are documented??"""

        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.aassertIsNotNone(BaseModel.__str__.__doc__)
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
        self.assetTrue(exe)


if __name__ = "__main__":
    unittest.main()
