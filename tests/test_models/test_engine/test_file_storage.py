#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import pep8
import unittest
from models import FileStorage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class Test_user(unittest.TestCase):
    """Test to check"""

    def test_pep8_file_storage(self):
        """Test PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors found.")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNotNone(file_storage.__doc__, "fix a docstring")


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_all_dict(self):
        """Test that returns the FileStorage.__objects"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)

    def test_new(self):
        """test that new adds an object"""
        objects = BaseModel()
        storage = FileStorage()
        storage.new(objects)
        self.assertNotEqual(storage.all(), 0)

    def test_save(self):
        """test save function"""
        objects = BaseModel()
        objects.name = "stranger"
        storage = FileStorage()
        objects.save()
        with open('file.json', 'r') as file:
            dic_json = json.load(file)
        val_dic = dic_json.get("BaseModel.{}".format(objects.id))
        self.assertEqual(val_dic['name'], "stranger")

    def test_reload(self):
        """test reload"""
        objects = BaseModel()
        storage = FileStorage()
        objects.name = "sober"
        objects.age = 23.45
        objects.save()
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_objects(self):
        """test if objects exists"""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_file_path(self):
        """test file path"""
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__file_path, str)
