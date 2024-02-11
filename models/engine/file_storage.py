#!/usr/bin/python3
"""file_storage: storing data"""

import json
import os
from models.base_model import BaseModel
from models.user import User

blueprint = {"BaseModel": BaseModel, "User": User}

class FileStorage():
    """serializeing instaces to a JSON file and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        falcon = self.__objects
        falcon_d = {obj: falcon[obj].to_dict() for obj in falcon.keys()}
        with open(self.__file_path, 'w') as file:
            json.dump(falcon_d, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path) as file:
                    file_dictionary = json.load(file)
                    for key, value in file_dictionary.items():
                        attribute = blueprint[value["__class__"]](**value)
                        self.__objects[key] = attribute
        except FileNotFoundError:
            pass
