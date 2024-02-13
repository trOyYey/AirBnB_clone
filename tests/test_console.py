#!/usr/bin/python3
"""Unittest for console.py"""

from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import unittest
import console
import tests
import os


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

