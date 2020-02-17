#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel

class TestBase(unittest.TestCase):

    def test_id_type(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.id),str)

    def test_id_diff(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_None(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsNotNone(b1.id)
        self.assertIsNotNone(b2.id)

    def test_attributes_vals(self):
        b1 = BaseModel()
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

    def test_update_format(self):
        b1 = BaseModel()
        b1.save()
        b1_json = b1.to_dict()
        u_date_obj = b1.updated_at
        u_date_obj2 = datetime.strptime(b1_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(u_date_obj, u_date_obj2)

    def test_create_format(self):
        try:
            b1 = BaseModel()
            b1.save()
            b1_json = b1.to_dict()
            b1.created_at.strptime(b1_json["created_at"],"%Y-%m-%dT%H:%M:%S.%f")

        except:
            self.assertRaises(ValueError, "Incorrect date (create) format")

    def test_create_from_dict1(self):
        b1 = BaseModel()
        b1.name = "Bob"
        b1.my_number = "213"
        b1.lname = "Smith"
        b1_json = b1.to_dict()

        b2 = BaseModel(**b1_json)

        self.assertEqual(b1.__dict__, b2.__dict__)

    def test_create_from_dict2(self):
        b1 = BaseModel()
        b1.name = "Rob"
        b1.my_number = "312"
        b1.lname = "Jones"
        b1_json = b1.to_dict()

        b2=BaseModel(**b1_json)

        output1 =StringIO()
        print(sorted(b1.__dict__.items()), file=output1, end='')
        content1 = output1.getvalue()
        output1.close()

        output2 =StringIO()
        print(sorted(b2.__dict__.items()), file=output2, end='')
        content2 = output2.getvalue()
        output2.close()

        self.assertEqual(content1, content2)

    def test_create_from_dict3(self):
        b1 = BaseModel()
        b1.name = "Peter"
        b1.my_number = "415"
        b1.lname = "Pico"
        b1_json = b1.to_dict()

        b2 = BaseModel(**b1_json)

        self.assertEqual(b1.__class__.__name__, b2.__class__.__name__)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.name, b2.name)
        self.assertEqual(b1.my_number, b2.my_number)
        self.assertEqual(b1.lname, b2.lname)
