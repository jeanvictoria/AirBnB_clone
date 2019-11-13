#!/usr/bin/python3
"""
Contains the Test classes
"""
 
from models import city
import pep8
import unittest 
from models.base_model import BaseModel
City = city.City

class Test_city(unittest.TestCase):
    """Test to check""" 
    
    def test_pep8_city(self):
        """test pep8 style""" 
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.") 
    
    def test_city_docstring(self):
        """test docstring"""
        self.assertIsNotNone(city.__doc__, "city.py needs docstring")

class Test_City(unittest.TestCase):
    """Test the class City"""
    
    def test_subclass(self):
        """Test if City is a BaseModel subclass"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name(self):
        """test if name is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_create_to_dict(self):
        """test to verified if the dic is created"""
        city = City()
        dict_new = city.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """test to verified de values in a dic"""
        city = City()
        dict_new = city.to_dict()
        self.assertEqual(dict_new["__class__"], "City")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_str(self):
        """test to verified if str has an correct input"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
