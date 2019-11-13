#!/usr/bin/python3
"""
Contains the Test classes
"""
 
from models import state
import pep8
import unittest 
from models.base_model import BaseModel
State = state.State

class Test_state(unittest.TestCase):
    """Test to check""" 
    
    def test_pep8_state(self):
        """test pep8 style""" 
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.") 
    def test_state_docstring(self):
        """test docstring"""
        self.assertIsNotNone(state.__doc__, "state.py needs docstring")

class Test_State(unittest.TestCase):
    """Test the class State"""
    
    def test_subclass(self):
        """Test if State is a BaseModel subclass"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name(self):
        """test if name is an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_create_to_dict(self):
        """test to verified if the dic is created"""
        state = State()
        dict_new = state.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """test to verified de values in a dic"""
        state = State()
        dict_new = state.to_dict()
        self.assertEqual(dict_new["__class__"], "State")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_str(self):
        """test to verified if str has an correct input"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))
