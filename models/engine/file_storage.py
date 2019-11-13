#!/usr/bin/python3
"""FileStorage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage():
    """Serialize and deserialize"""

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}

    # string-path to the JSON file
    __file_path = "file.json"
    # dictionary
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize __objects to de JSON file """
        j_objects = {}
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(j_objects, file)

    def reload(self):
        """deserialize the JSON file to __objects """
        try:
            with open(self.__file_path) as file:
                reloaded = json.loads(file.read())
                for key, value in reloaded.items():
                    class_name = key.split('.')[0]
                    obj = models.classes[class_name](**value)
                    self.__objects[key] = obj
        except IOError:
            pass

    def destroy(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        del(self.__objects[key])
        self.save()

    def update(self, obj, att, val):
        key = obj.__class__.__name__ + "." + obj.id
        setattr(obj, att, val)
        self.save()
