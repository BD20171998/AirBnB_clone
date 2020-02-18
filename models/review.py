#!/usr/bin/python3
'''
The User module
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A Review class that inherits BaseModel
    '''
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        '''Initializes an instance'''
        super().__init__(*args, **kwargs)
