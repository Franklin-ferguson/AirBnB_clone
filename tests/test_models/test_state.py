#!/usr/bin/python3
"""test for State"""
import unittest
import models
from models.state import State
from datetime import datetime
import os
from time import sleep


class TestState(unittest.TestCase):

    def test_inputs(self):
        self.assertIn(State(), models.storage.all().values())

        self.assertEqual(State, type(State))
        
        self.assertEqual(str, type(State.id))
        
        self.assertEqual(datetime, type(State.created_at))

        self.assertEqual(datetime, type(State.updated_at))

    def test_name(self):
        state_1 = State()
        
        self.assertIn("name",dir(state_1))
        self.assertEqual(str, type(State.name))
        self.assertNotIn("name", state_1.__dict__)

    def test_state_not_the_same(self):
        state_1 = State()
        sleep(0.10)
        state_2 = State()

        self.assertNotEqual(state_1, state_2)
        
        self.assertLess(state_1.created_up, state_2.created_up)
        self.assertLess(state_1.updated_up, state_2.updated_up)












if __name__ == "__main__":
    unittest.main()
    


