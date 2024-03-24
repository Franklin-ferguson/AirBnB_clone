#!/usr/bin/python3
import unittest
import os
import models
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User"""

    def setUp(self):
        self.test_file_path = "test_file.json"
        models.storage.__file_path = self.test_file_path
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_user_attributes(self):

        test_User = User()
        self.assertEqual(test_User.email, "")
        self.assertEqual(test_User.password, "")
        self.assertEqual(test_User.first_name, "")
        self.assertEqual(test_User.last_name, "")

    def test_user_inheritance(self):

        test_User = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str(self):

        test_User = User()

        test_User.email = "frankliny@gmail.com"
        test_User.password = "abcdef123456"
        test_User.first_name = "Franklin"
        test_User.last_name = "Yesutor"

        User_str = str(test_User)
        self.assertIn("User", User_str)
        self.assertIn("frankliny@gmail.com", User_str)
        self.assertIn("Franklin", User_str)
        self.assertIn("Yesutor", User_str)

    def test_user_to_dict(self):

        test_User = User()

        test_User.email = "frankliny@gmail.com"
        test_User.password = "abcdef123456"
        test_User.first_name = "Franklin"
        test_User.last_name = "Yesutor"
        test_User.save()
        
        user_to_dict = test_User.to_dict()
        self.assertEqual(user_to_dict["email"], "frankliny@gmail.com")
        self.assertEqual(user_to_dict["first_name"], "Franklin")

        self.assertEqual(user_to_dict["last_name"], "Yesutor")

    def test_user_instance(self):

        test_User = User(
            email="frankliny@gmail.com",
            password="abcdef123456",
            first_name="Franklin",
            last_name="Yesutor",
        )

        self.assertEqual(test_User.email, "frankliny@gmail.com")
        self.assertEqual(test_User.password, "abcdef123456")
        self.assertEqual(test_User.first_name, "Franklin")
        self.assertEqual(test_User.last_name, "Yesutor")
        
        user_to_dict = test_User.to_dict()
        self.assertEqual(user_to_dict["email"], "frankliny@gmail.com")
        self.assertEqual(user_to_dict["password"], "abcdef123456")

        self.assertEqual(user_to_dict["first_name"], "Franklin")

        self.assertEqual(user_to_dict["last_name"], "Yesutor")

    def test_user_id(self):

        User1 = User()
        User2 = User()

        self.assertNotEqual(User1, User2)


if __name__ == "__main__":
    unittest.main()
