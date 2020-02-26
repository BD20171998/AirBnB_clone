#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from io import StringIO
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestBase(unittest.TestCase):

    def test_user_type(self):
        b1 = User()
        self.assertEqual(type(b1), User)

    def test_user_attrs(self):
        b3 = User()
        b3.first_name = "Betty"
        b3.last_name = "Holberton"
        b3.email = "airbnb@holbertonshool.com"
        b3.password = "root"

        self.assertEqual(type(b3.first_name), str)
        self.assertEqual(type(b3.last_name), str)
        self.assertEqual(type(b3.email), str)
        self.assertEqual(type(b3.password), str)

        self.assertEqual(b3.first_name, "Betty")
        self.assertEqual(b3.last_name, "Holberton")
        self.assertEqual(b3.email, "airbnb@holbertonschool.com")
        self.assertEqual(b3.password, "root")
