#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

#storage = FileStorage()

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
