#!/usr/bin/python3
import json

class FileStorage():
    """serializeing instaces to a JSON file and deserializing JSON file to instances"""
    def __init__(self, file_path="file.json"):
        """initialising:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
        """
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if self.__file_path:
            self.__objects = json.load(self.__file_path)

