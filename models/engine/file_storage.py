#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage():
    """serializeing instaces to a JSON file and deserializing JSON file to instances"""
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
        """ serializes __objects to the JSON file (path: __file_path)"""
        falcon = self.__objects
        falcon_dictionary = {obj : falcon[obj].to_dict() for obj in falcon.keys()}
        with open(self.__file_path, 'w') as file:
            json.dump(falcon_dictionary, file)
    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                falcon_dictionary = json.load(file)
                for obj_dict in falcon_dictionary.values():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
