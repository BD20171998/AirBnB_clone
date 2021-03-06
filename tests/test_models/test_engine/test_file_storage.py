#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os.path

class TestFileStorage(unittest.TestCase):

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

    def test_save_file(self):
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

        with open('file.json', 'r') as f:
            str_objs = json.load(f)

        key = "BaseModel" + "." + self.b1.id
        obj = str_objs[key]

        self.assertEqual(dict1, obj)

    def test_reload2(self):
        self.b1 = BaseModel()
        self.b1.save()
        dict1 = self.b1.to_dict()
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        all_objs = self.storage.all()
        key = "BaseModel" + "." + self.b1.id
        obj = all_objs[key]
        dict2 = obj.to_dict()

        self.assertEqual(dict1, dict2)

    def test_save(self):
        self.b1 = BaseModel()
        self.b1.name = "George Washington"
        self.b1.my_number = 90
        self.b2 = BaseModel()

        self.storage.new(self.b1)
        self.storage.new(self.b2)

        self.storage.save()

        all_obj = {k:v.to_dict() for k,v in self.storage.all().items()}

        with open('file.json', 'r') as f:
            str_objs = json.loads(f.read())

        self.assertEqual(all_obj, str_objs)
