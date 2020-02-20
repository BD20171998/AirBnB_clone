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

    def test_user(self):
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"

        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Holberton")
        self.assertEqual(my_user.email, "airbnb@holbertonshool.com")
        self.assertEqual(my_user.password, "root")

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
