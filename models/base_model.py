#!/usr/bin/python3
"""
defining BaseModel class"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """ BaseModel is a class that defines
    the information of something using id
    created_at and updated_at and then
    the information like name etc"""

    def __init__(self, *args, **kwargs):
        """
        id: string - assign with an uuid when an instance is created
        created_at: datetime
        updated_at: datetime - assign with the current datetime"""
        ash = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, ash)
                    setattr(self, key, value)

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save(self): updates the public instance attributes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dictionnary = self.__dict__.copy()
        dictionnary["__class__"] = self.__class__.__name__
        dictionnary["created_at"] = self.created_at.isoformat()
        dictionnary["updated_at"] = self.updated_at.isoformat()
        return dictionnary
