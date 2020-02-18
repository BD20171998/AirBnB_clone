#!/usr/bin/python3
'''
The User module
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    A Amenity class that inherits BaseModel
    '''
    name = ''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance'''
        super().__init__(*args, **kwargs)
