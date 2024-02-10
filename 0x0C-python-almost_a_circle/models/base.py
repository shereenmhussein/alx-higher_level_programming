#!/usr/bin/python3
'''Module for Base class.'''

class Base:
    '''A representation of the base of our OOP heirarchy.'''

    __nb_objects = 0

    def__init__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
