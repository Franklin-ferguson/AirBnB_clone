#!/usr/bin/python3
"""test for city"""
import unittest
import models
from models.city import city
from datetime import datetime
import os
from time import sleep


class TestState(unittest.TestCase):

    def test_inputs(self):
        self.assertIn(City()), models.storage.all().values())

        self.assertEqual(City, type(City))
        
        self.assertEqual(str, type(City.id))
        
        self.assertEqual(datetime, type(City.created_at))

        self.assertEqual(datetime, type(City.updated_at))

    def test_name(self):
        city_1 = City()
        
        self.assertIn("name",dir(city_1))
        self.assertEqual(str, type(city_1.name))
        self.assertNotIn("name", city_1.__dict__)

    def test_state_not_the_same(self):
        city_1 = City()
        sleep(0.10)
        city_2 = City()

        self.assertNotEqual(city_1, city_2)
        
        self.assertLess(city_1.created_up, city_2.created_up)
        self.assertLess(city_1.updated_up, city_2.updated_up)












if __name__ == "__main__":
    unittest.main()
    


