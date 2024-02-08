#!/usr/bin/python3
import uuid
from datetime import datetime
from __init__ import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
        """
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every
        time you change your object"""
        if kwargs is not None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save(self): updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionnary = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictionnary[key] = value.isoformat()
            else:
                dictionnary[key] = value
        return dictionnary
