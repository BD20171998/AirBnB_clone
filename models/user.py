#!/usr/bin/python3
'''
The User module
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    A User class that inherits BaseModel
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance'''
        super().__init__(*args, **kwargs)
