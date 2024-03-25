#!/usr/bin/python3
"""test for Place"""
import unittest
import models
from models.state import Place
from datetime import datetime
import os
from time import sleep


class TestPlace(unittest.TestCase):

    def test_inputs(self):
        self.assertIn(Place(), models.storage.all().values())

        self.assertEqual(State, type(Place))
        
        self.assertEqual(str, type(Place.id))
        
        self.assertEqual(datetime, type(Place.created_at))

        self.assertEqual(datetime, type(Place.updated_at))

    def test_name(self):
        place_1 = Place()
        
        self.assertIn("name",dir(place_1))
        self.assertEqual(str, type(place.name))
        self.assertNotIn("name", place_1.__dict__)

    def test_place_not_the_same(self):
        place_1 = Place()
        sleep(0.10)
        place_2 = Place()

        self.assertNotEqual(place_1, place_2)
        
        self.assertLess(place_1.created_up, place_2.created_up)
        self.assertLess(place_1.updated_up, place_2.updated_up)












if __name__ == "__main__":
    unittest.main()
    


