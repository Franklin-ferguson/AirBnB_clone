#!/usr/bin/python3
"""test for Review"""
import unittest
import models
from models.review import Review
from datetime import datetime
import os
from time import sleep


class TestReview(unittest.TestCase):

    def test_inputs(self):
        self.assertIn(Review(), models.storage.all().values())

        self.assertEqual(State, type(Review))
        
        self.assertEqual(str, type(Review.id))
        
        self.assertEqual(datetime, type(Review.created_at))

        self.assertEqual(datetime, type(Review.updated_at))

    def test_name(self):
        review_1 = Review()
        
        self.assertIn("name",dir(review_1))
        self.assertEqual(str, type(Review.name))
        self.assertNotIn("name", review_1.__dict__)

    def test_review_not_the_same(self):
        review_1 = Review()
        sleep(0.10)
        review_2 = Review()

        self.assertNotEqual(review_1, review_2)
        
        self.assertLess(review_1.created_up, review_2.created_up)
        self.assertLess(review_1.updated_up, review_2.updated_up)












if __name__ == "__main__":
    unittest.main()
    


