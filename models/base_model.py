#!/usr/bin/python3
"""
class BaseModel
"""

from datetime import datetime
from uuid import uuid4

tm = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:

    def __init__(self, *args, **kwargs):
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
                if key == "created_at":
                    self.created_at = datetime.strptime(value, tm)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, tm)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_new = self.__dict__.copy()
        dict_new["__class__"] = self.__class__.__name__
        if "created_at" in dict_new:
            dict_new["created_at"] = self.created_at.isoformat()
        if "updated_at" in dict_new:
            dict_new["updated_at"] = self.updated_at.isoformat()

        return dict_new
