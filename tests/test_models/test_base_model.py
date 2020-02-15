#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel

class TestBase(unittest.TestCase):

    def setUp(self):

    def test_id_type:
        my_model = BaseModel()
        self.assertEqual(type(my_model.id),str)

    def test_id_diff:
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_None:
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(my_model.id)

    def test_attributes_vals:
        b1.name = "Kev"
        b1.my_number = "708"
        update_date = b1.updated_at
        create_date = b1.created_at

        self.assertEqual(b1.my_number, "708")
        self.assertEqual(b1.name, "Kev")
        self.assertEqual(b1.__class__.__name__, "BaseModel")

        b1.save()
        create_date2 = b1.created_at
        update_date2 = b1.updated_at
        self.assertEqual(create_date, create_date2)
        self.assertNotEqual(update_date, update_date2)

    def test_update_format:
        try:
            u_date_str = b1.updated_at
            u_date_obj = datetime.strptime(u_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        except:
            self.assertRaises(ValueError, "Incorrect date (update) format")

    def test_create_format:
        try:
            c_date_str = b1.created_at
            c_date_obj = datetime.strptime(c_date_str, "%Y-%m-%dT%H:%M:%S.%f")

        except:
             self.assertRaises(ValueError, "Incorrect date (create) format")
