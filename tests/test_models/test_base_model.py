#!/usr/bin/python3
""" Test for BaseModel"""
import unittest
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''Test BaseModel'''

        def test_save(self):
        '''test save attribute'''
        self.before = self.my_model.updated_at
        self.my_model.save()
        self.after = self.my_model.updated_at
        self.assertIsNot(self.before, self.after)

if __name__ == '__main__':
    unittest.main()
