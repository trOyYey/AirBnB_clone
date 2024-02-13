#!/usr/bin/python3
"""Unittest for console.py"""

from unittest.mock import patch, MagicMock
from console import HBNBCommand
from io import StringIO
import unittest
import console
import tests
import os
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """testing the console"""

    @classmethod
    def setUpClass(instance):
        """setting variables for console """
        instance.console = HBNBCommand()

    @classmethod
    def teardown(instance):
        """removing setup variables"""
        del instance.console
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def all(cls):
        return list(cls.__objects.values())

    def test_doc_strings(self):
        """ everything is docummented??"""

        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)

    def test_emptyline(self):
        """testing emptyline command"""

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertNotEqual(f.getvalue().strip(), "** class name missing **")
            self.assertNotEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertNotEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as O:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected, O.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as O:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(expected, O.getvalue().strip())

    def test_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected, o.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(expected, o.getvalue().strip())
if __name__ == "__main__":
    unittest.main()

