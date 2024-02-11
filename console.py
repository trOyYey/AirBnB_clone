#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    def preloop(self):
        """Prints when isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
