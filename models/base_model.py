#!/usr/bin/env python3
'''
The Base Model Module
'''
from datetime import datetime
import uuid


class BaseModel:
    '''A BaseModel Module'''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance'''
        if len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'name' in kwargs:
                self.name = kwargs['name']

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = str(self.__class__.__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
