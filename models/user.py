#!/usr/bin/python3
from base_model import BaseModel


'''
This is the 'user' module.

user contains one class: 'User', which inherits from the BaseModel class.

'''


class User(BaseModel):
    '''This is the 'User' class.
    User contains the attributes: email, password, first_name, last_name.
    '''
    def __init__(self):
        '''This is the initialization function.
        initializes User with class attributes set to empty strings.
        '''
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''