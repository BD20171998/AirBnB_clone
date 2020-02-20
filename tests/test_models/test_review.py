#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from io import StringIO
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b2 = Review()
        self.b4 = BaseModel()

    def test_id_diff(self):
        self.assertNotEqual(self.b4.id, self.b2.id)

    def test_id_None(self):
        self.assertIsNotNone(self.b4.id)
        self.assertIsNotNone(self.b2.id)

    def test_review_default(self):
        self.assertEqual(self.b2.user_id, '')

    def test_review_type(self):
        self.assertEqual(type(self.b2.user_id), str)

    def test_str(self):
        self.b2.text = "Don't stay here!!!!"
        teststr = "[Review] ({}) {}".format(self.b2.id, self.b2.__dict__)
        self.assertEqual(teststr, str(self.b2))

    def test_update_format(self):
        self.b2.save()
        b1_json = self.b2.to_dict()
        u_date_obj = self.b2.updated_at
        u_date_obj2 = datetime.strptime(b1_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(u_date_obj, u_date_obj2)
