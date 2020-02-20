#!/usr/bin/python3
"""
Unittest for BaseModel class
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


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b1 = Place()
        self.b2 = State()
        self.b3 = User()
        self.b4 = BaseModel()

    def test_id_diff(self):
        self.assertNotEqual(self.b4.id, self.b3.id)

    def test_id_None(self):
        self.assertIsNotNone(self.b4.id)
        self.assertIsNotNone(self.b2.id)

    def test_place_default(self):
        self.assertEqual(self.b1.city_id, '')
        self.assertEqual(self.b1.user_id, '')
        self.assertEqual(self.b1.name, '')
        self.assertEqual(self.b1.description, '')
        self.assertEqual(self.b1.number_rooms, 0)
        self.assertEqual(self.b1.number_bathrooms, 0)
        self.assertEqual(self.b1.max_guest, 0)
        self.assertEqual(self.b1.price_by_night, 0)
        self.assertEqual(self.b1.latitude, 0.0)
        self.assertEqual(self.b1.longitude, 0.0)
        self.assertEqual(self.b1.amenity_ids, [])

    def test_place_type(self):
        self.assertEqual(type(self.b1.city_id), str)
        self.assertEqual(type(self.b1.user_id), str)
        self.assertEqual(type(self.b1.name), str)
        self.assertEqual(type(self.b1.description), str)
        self.assertEqual(type(self.b1.number_rooms), int)
        self.assertEqual(type(self.b1.number_bathrooms), int)
        self.assertEqual(type(self.b1.max_guest), int)
        self.assertEqual(type(self.b1.price_by_night), int)
        self.assertEqual(type(self.b1.latitude), float)
        self.assertEqual(type(self.b1.longitude), float)
        self.assertEqual(type(self.b1.amenity_ids), list)

    def test_str(self):
        self.b3.first_name = "Jon"
        teststr = "[User] ({}) {}".format(self.b3.id, self.b3.__dict__)
        self.assertEqual(teststr, str(self.b3))

    def test_update_format(self):
        self.b1.save()
        b1_json = self.b1.to_dict()
        u_date_obj = self.b1.updated_at
        u_date_obj2 = datetime.strptime(b1_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(u_date_obj, u_date_obj2)
