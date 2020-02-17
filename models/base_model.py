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
            for k in kwargs.keys():

                if k == '__class__':
                    continue

                if k == 'created_at':
                    self.__dict__[k] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    continue

                if k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    continue

                self.__dict__[k] = kwargs[k]

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
