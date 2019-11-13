#!/usr/bin/python3
"""
Contains the Test classes
"""
 
from models import review
import pep8
import unittest 
from models.base_model import BaseModel
Review = review.Review

class Test_review(unittest.TestCase):
    """Test to check""" 
    
    def test_pep8_review(self):
        """test pep8 style""" 
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Code style errors founded.") 
    
    def test_review_docstring(self):
        """test docstring"""
        self.assertIsNotNone(review.__doc__, "review.py needs docstring")

class Test_Review(unittest.TestCase):
    """Test the class Review"""
    
    def test_subclass(self):
        """Test if Review is a BaseModel subclass"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_text(self):
        """test if text is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_place_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """test user_id"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_create_to_dict(self):
        """test to verified if the dic is created"""
        review = Review()
        dict_new = review.to_dict()
        self.assertEqual(type(dict_new), dict)

    def test_values_to_dict(self):
        """test to verified de values in a dic"""
        review = Review()
        dict_new = review.to_dict()
        self.assertEqual(dict_new["__class__"], "Review")
        self.assertEqual(type(dict_new["created_at"]), str)
        self.assertEqual(type(dict_new["updated_at"]), str)
        self.assertEqual(type(dict_new["id"]), str)

    def test_str(self):
        """test to verified if str has an correct input"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
