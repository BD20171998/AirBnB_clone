#!/usr/bin/env python3
'''
The File Storage Module
'''
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
import json

class FileStorage:
    '''A FileStorage Module'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with file <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        new_dict = {}

        for k, v in self.__objects.items():

            new_dict[k] = self.__objects[k].to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
            json.dump(new_dict, a_file)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as a_file:
                str_objs = json.load(a_file)

                for key, val in str_objs.items():
                    cls_name = val['__class__']
                    self.__objects[key] = eval(cls_name)(**val)
        except:
            pass
