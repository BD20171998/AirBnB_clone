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
        self.assertIsNotNone(self.b1.id)
        self.assertIsNotNone(self.b2.id)

    def test_user_attr(self):
        self.b4 = User()
        self.b4.first_name = "Betty"
        self.b4.last_name = "Holberton"
        self.b4.email = "airbnb@holbertonshool.com"
        self.b4.password = "root"

        self.assertEqual(self.b4.first_name, "Betty")
        self.assertEqual(self.b4.last_name, "Holberton")
        self.assertEqual(self.b4.email, "airbnb@holbertonshool.com")
        self.assertEqual(self.b4.password, "root")

    def test_user_types(self):
        self.b3 = User()
        self.b3.first_name = "Betty"
        self.b3.last_name = "Holberton"
        self.b3.email = "airbnb@holbertonshool.com"
        self.b3.password = "root"

        self.assertEqual(type(self.b3.first_name), str)
        self.assertEqual(type(self.b3.last_name), str)
        self.assertEqual(type(self.b3.email), str)
        self.assertEqual(type(self.b3.password), str)

    def test_str(self):
        self.b2.first_name = "Roger"
        teststr = "[User] ({}) {}".format(self.b2.id, self.b2.__dict__)
        self.assertEqual(teststr, str(self.b2))

    def test_update_format(self):
        self.b2.save()
        b1_json = self.b2.to_dict()
        u_date_obj = self.b2.updated_at
        u_date_obj2 = datetime.strptime(b1_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(u_date_obj, u_date_obj2)
