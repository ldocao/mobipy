# -*- coding: utf-8 -*-

from abc import ABCMeta


class Accomodation(metaclass = ABCMeta):
    counter = 0
    
    def __init__(self):
        self._id = self.create_unique_id()
        self.metadata = None
        self.interior = None

        
    @classmethod
    def create_unique_id(cls):
        cls.counter += 1
        return cls.counter

    
    def __repr__(self):
        return self.__class__.__name__


    

class Apartment(Accomodation):
    pass

    
# class House(Accomodation):
#     raise NotImplementedError


# class SharedAccomodation(Accomodation):
#     """Room inside a shared house"""
#     raise NotImplementedError

    
# class SharedRoom(Accomodation):
#     """Room in which several persons live"""
#     raise NotImplementedError
            
