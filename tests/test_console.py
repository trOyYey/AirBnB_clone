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
