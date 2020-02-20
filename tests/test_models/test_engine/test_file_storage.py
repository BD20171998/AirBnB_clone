#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os.path

class TestBase(unittest.TestCase):

    def setUp(self):
        open('file.json', 'w').close()
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        self.b1 = BaseModel()
        self.b1.name = "Holberton"
        self.b1.my_number = 89
        self.b1.save()

        self.assertEqual(type(self.storage.all()), dict)

    def test_dict(self):
        self.b1 = BaseModel()
        self.b1.name = "Holberton"
        self.b1.my_number = 89
        self.b1.save()

        dict1 = self.b1.to_dict()

        all_objs = self.storage.all()

        key = "BaseModel" + "." + self.b1.id
        obj = all_objs[key]
        dict2 = obj.to_dict()
        self.assertEqual(dict1, dict2)

    def test_save(self):
        self.b1 = BaseModel()
        self.b1.name = "George Washington"
        self.b1.my_number = 908
        self.b1.save()

        self.assertTrue(os.path.isfile('file.json'))

    def test_reload(self):
        self.b1 = BaseModel()
        self.b1.save()
        all_objs = self.storage.all()
        key = "BaseModel" + "." + self.b1.id
        obj = all_objs[key]
        dict1 = obj.to_dict()
        self.assertEqual(type(dict1), dict)

    def test_save_base(self):
        self.b1 = BaseModel()
        self.b1.save()
        dict1 = self.b1.to_dict()

        all_objs = self.storage.all()
        key = "BaseModel" + "." + self.b1.id
        obj = all_objs[key]
        dict2 = obj.to_dict()

        self.assertEqual(dict1, dict2)
