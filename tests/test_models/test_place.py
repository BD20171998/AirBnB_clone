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
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestBase(unittest.TestCase):


    def test_id_diff(self):
        b1 = BaseModel()
        b2 = User()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_None(self):
        b1 = BaseModel()
        b2 = State()
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b2.id)

    def test_place_default(self):
        b1 = Place()

        self.assertEqual(b1.city_id, '')
        self.assertEqual(b1.user_id, '')
        self.assertEqual(b1.name, '')
        self.assertEqual(b1.description, '')
        self.assertEqual(b1.number_rooms, 0)
        self.assertEqual(b1.number_bathrooms, 0)
        self.assertEqual(b1.max_guest, 0)
        self.assertEqual(b1.price_by_night, 0)
        self.assertEqual(b1.latitude, 0.0)
        self.assertEqual(b1.longitude, 0.0)
        self.assertEqual(b1.amenity_ids, [])

    def test_place_default(self):
        b1 = Place()

        self.assertEqual(type(b1.city_id), str)
        self.assertEqual(type(b1.user_id), str)
        self.assertEqual(type(b1.name), str)
        self.assertEqual(type(b1.description), str)
        self.assertEqual(type(b1.number_rooms), int)
        self.assertEqual(type(b1.number_bathrooms), int)
        self.assertEqual(type(b1.max_guest), int)
        self.assertEqual(type(b1.price_by_night), int)
        self.assertEqual(type(b1.latitude), float)
        self.assertEqual(type(b1.longitude), float)
        self.assertEqual(type(b1.amenity_ids), list)
