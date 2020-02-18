#!/usr/bin/python3
'''
The User module
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    A City class that inherits BaseModel
    '''
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance'''
        super().__init__(*args, **kwargs)
