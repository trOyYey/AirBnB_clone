#!/usr/bin/python3
"""Unittest for console.py"""

import console
import unittest


class TestConsole(unittestTestCase):
    """testing the console"""

    @classmethod
    def setUpClass(instance):
        """setting variables for console """
        instance.console = HBNBCommand()

    @classmethod
    def teardown(instance):
        """removing setup variables"""
        def instance.console
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc_strings(self):
        """ everything is docummented??"""

        sef.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)

    def test_emptyline(self):
        """testing emptyline command"""

        with patch("sys.stdout", new=stringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), "")
