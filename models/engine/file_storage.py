#!/usr/bin/env python3
'''
The File Storage Module
'''

import json
class FileStorage:
    '''A FileStorage Module'''

    __file_path = "kev.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = self.__class__.__name__ + '.' + self.id
        __objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file'''
        n_dict = __objects.copy()
        dict_str = json.dumps(n_dict)

        with open(self.__file_path, mode='a+', encoding='utf-8') as a_file:
            a_file.write(dict_str)

        print('WROTEEEEEEEEEEEE TO FILEEEEEEEEEEEEEEEEEEEEE')
    def reload(self):
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as a_file:
                str_objs = a_file.read()

            __objects = JSON.loads(str_objs)
        except:
            print('NO FILEEEEEEEEEEEEE@!')
            pass
