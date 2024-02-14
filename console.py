#!/usr/bin/python3
""" HBNB cmd class """
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import cmd
import sys

blueprint = {"BaseModel": BaseModel, "User": User, "State": State,
             "City": City, "Amenity": Amenity, "Place": Place,
             "Review": Review}


class HBNBCommand(cmd.Cmd):
    """airBNB main command interpreter class"""

    prompt = "(hbnb) "

    def default(self, arg):
        """default function when no command recognized"""
        if '(' not in arg or ')' not in arg or '.' not in arg:
            cmd.Cmd.default(self, arg)
            return
        class_var = arg.split('.')[0]
        command_var = arg.split('.')[1]
        command_var = command_var.split('(')[0]
        argument_var = arg.split('(')[1]
        argument_var = argument_var.split(')')[0]
        '''if '"' in argument_var:
            argument_var = argument_var.replace('"', '')'''
        argument_var = argument_var.split(',')
        if len(argument_var) >= 2 and argument_var[1].strip()[0] == '{':
            argument_var = [argument_var[0], ','.join(argument_var[1:])]
        cmd_dict = {"all": self.do_all, "count": self.do_count,
                    "show": self.do_show, "destroy": self.do_destroy,
                    "update": self.do_update}
        if command_var in cmd_dict:
            cmd_dict[command_var](class_var + ' ' + ' '.join(argument_var))
        else:
            cmd.Cmd.default(self, arg)

    def do_count(self, arg):
        """counts active objects and prints the result"""
        argument_var = arg.split()
        if len(argument_var) == 0:
            print("** class name missing **")
        elif argument_var[0] not in blueprint:
            print("** class doesn't exist **")
        else:
            dict_var = storage.all()
            counter = 0
            for key in dict_var:
                if argument_var[0] == key.split('.')[0]:
                    counter = counter + 1
            print(counter)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit when end of file"""
        return True

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_create(self, arg):
        '''creates new instance of class'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        else:
            new_b = blueprint[args[0]]()
            storage.save()
            print(new_b.id)

    def help_create(self):
        """Documentation for how create works"""
        print("Creates a new instance of the specified class Class,")
        print("saves it to the JSON file and prints the id.")
        print("Usage: Create <className>\n")

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in obj_dict:
                print(obj_dict[key])
            else:
                '''print(f'{key}')'''
                print("** no instance found **")

    def help_show(self):
        """Documentation for how show is executed"""
        print("Prints the string representation of instance")
        print("based on the class name and id.")
        print("Usage: show <className> <id>\n")

    def do_destroy(self, arg):
        '''completely delete specified instance given by class and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """Documentation for how destroy is executed"""
        print("Deletes an instance based on the class name and id,")
        print("(saves the change into the JSON file).")
        print("Usage: destroy <className> <id>\n")

    def do_all(self, arg):
        '''Prints __str__ of all instances'''
        args = arg.split()
        obj_dict = storage.all()
        string = []
        if len(args) != 0:
            if args[0] not in blueprint:
                print("** class doesn't exist **")
                return
            else:
                for key in obj_dict:
                    if obj_dict[key].__class__.__name__ == args[0]:
                        string.append(str(obj_dict[key]))
        else:
            for key in obj_dict:
                string.append(str(obj_dict[key]))
        print(string)

    def help_all(self):
        '''Documentation for how all is executed'''
        print("Prints all string representation of all instances")
        print("based or not on the class name.")
        print("Usage: all <className> OR all\n")

    def do_update(self, arg):
        '''updates an instance using user input'''
        args = arg.split()
        dict_indicator = 0
        if len(args) > 3 and args[2].strip()[0] == '{':
            dict_indicator = 1
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = obj_dict[f"{args[0]}.{args[1]}"]
            if dict_indicator != 1:
                args[3] = args[3].strip("\"\'")
                if args[2] in instance.__dict__:
                    args[3] = type(instance.__dict__[args[2]])(args[3])
                instance.__dict__[args[2]] = args[3]
            else:
                self.update_dict(instance, args[2:])
            instance.save()
            storage.save()

    def update_dict(self, instance, args):
        """updating class instances with dict arguments"""
        for i in range(0, len(args), 2):
            if (i + 1 == len(args)):
                return
            '''print(f'{args[i]}')'''
            args[i] = args[i].strip("{:")
            args[i] = args[i].strip('\'\"')
            args[i + 1] = args[i + 1].strip("},)")
            '''print(f'{args[i + 1]}')'''
            args[i + 1] = args[i + 1].strip('\"\'')
            args[i + 1] = args[i + 1].strip("\"\')")
            '''print(f'{args[i + 1]}')'''
            if args[i] in instance.__dict__:
                args[i + 1] = type(instance.__dict__[args[i]])(args[i + 1])
            instance.__dict__[args[i]] = args[i + 1]

    def help_update(self):
        '''Documentation for how update is executed'''
        print("Updates an instance based on the class name and id")
        print("adding or updating attribute (saves changes to JSON file)")
        print("Usage: update <class name> <id> <att name> \"<att value>\"\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
