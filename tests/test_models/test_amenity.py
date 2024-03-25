#!/usr/bin/python3
"""test for amenity"""
import unittest
import models
from models.amenity import Amenity
from datetime import datetime
import os
from time import sleep


class TestState(unittest.TestCase):

    def test_inputs(self):
        self.assertIn(Amenity(), models.storage.all().values())

        self.assertEqual(Amenity, type(Amenity))
        
        self.assertEqual(str, type(Amenity.id))
        
        self.assertEqual(datetime, type(Amenity.created_at))

        self.assertEqual(datetime, type(Amenity.updated_at))

    def test_name(self):
        amenity_1 = Amenity()
        
        self.assertIn("name", dir(amenity_1))
        self.assertEqual(str, type(Amenity.name))
        self.assertNotIn("name", amenity_1.__dict__)

    def test_state_not_the_same(self):
        state_1 = State()
        sleep(0.10)
        state_2 = State()

        self.assertNotEqual(state_1, state_2)
        
        self.assertLess(state_1.created_up, state_2.created_up)
        self.assertLess(state_1.updated_up, state_2.updated_up)












if __name__ == "__main__":
    unittest.main()
    


