#!/usr/bin/python3
"""
Contains the Test classes
"""
 
from models import amenity
import pep8
import unittest 
from models.base_model import BaseModel
Amenity = amenity.Amenity

class Test_state(unittest.TestCase):
    """Test to check""" 
    
    def test_pep8_amenity(self):
        """test pep8 style""" 
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.") 
    def test_state_docstring(self):
        """test docstring"""
        self.assertIsNotNone(amenity.__doc__, "amenity.py needs docstring")

class Test_Amenity(unittest.TestCase):
    """Test the class Amenity"""
    
    def test_subclass(self):
        """Test if Amenity is a BaseModel subclass"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name(self):
        """test if name is an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_create_to_dict(self):
        """test to verified if the dic is created"""
        amenity = Amenity()
        dict_new = amenity.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """test to verified de values in a dic"""
        amenity = Amenity()
        dict_new = amenity.to_dict()
        self.assertEqual(dict_new["__class__"], "Amenity")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_str(self):
        """test to verified if str has an correct input"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
