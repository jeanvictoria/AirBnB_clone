#!/usr/bin/python3
""" Test for BaseModel"""
import pep8
import unittest
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Test BaseModel'''

        def test_pep8_state(self):
        """test pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.") 

        def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        def test_doc_module(self):
        '''validate documentation module'''
        document = models.base_model.__doc__
        self.assertIsNotNone(document)

        def test_doc_module(self):
        '''validate documentation class'''
        document = BaseModel.__doc__
        self.assertIsNotNone(document)

        def test_save(self):
        '''test save attribute'''
        self.before = self.my_model.updated_at
        self.my_model.save()
        self.after = self.my_model.updated_at
        self.assertIsNot(self.before, self.after)

if __name__ == '__main__':
    unittest.main()
