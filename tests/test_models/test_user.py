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

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = User()

    def test_id_diff(self):
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_id_None(self):
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b2.id)

    def test_user_attr(self):
        self.b2.first_name = "Betty"
        self.b2.last_name = "Holberton"
        self.b2.email = "airbnb@holbertonshool.com"
        self.b2.password = "root"

        self.assertEqual(self.b2.first_name, "Betty")
        self.assertEqual(self.b2.last_name, "Holberton")
        self.assertEqual(self.b2.email, "airbnb@holbertonshool.com")
        self.assertEqual(self.b2.password, "root")

    def test_user_types(self):
        self.b2.first_name = "Betty"
        self.b2.last_name = "Holberton"
        self.b2.email = "airbnb@holbertonshool.com"
        self.b2.password = "root"

        self.assertEqual(type(self.b2.first_name), str)
        self.assertEqual(type(self.b2..last_name), str)
        self.assertEqual(type(self.b2.email), str)
        self.assertEqual(type(self.b2.password), str)

    def test_str(self):
        self.b2.first_name = "Roger"
        teststr = "[City] ({}) {}".format(self.b2.id, self.b2.__dict__)
        self.assertEqual(teststr, str(self.b2))

    def test_update_format(self):
        self.b2.save()
        b1_json = self.b2.to_dict()
        u_date_obj = self.b2.updated_at
        u_date_obj2 = datetime.strptime(b1_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(u_date_obj, u_date_obj2)
