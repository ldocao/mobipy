# -*- coding: utf-8 -*-

from abc import ABCMeta


class Accomodation(metaclass = ABCMeta):
    counter = 0
    
    def __init__(self):
        self._id = self.create_new_id()
        self.metadata = self.metadata()
        self.interior = self.interior()

    @classmethod
    def create_new_id(cls):
        cls.counter += 1
        return cls.counter

    
    def metadata(self, metadata):
        pass ## children must implement this polymorphic method


    def interior(self, interior):
        pass ## children must implement this polymorphic method


    
    def __repr__(self):
        return self.__class__.__name__


    

class Apartment(Accomodation):
    
    def metadata(self):
        pass

    def interior(self):
        pass


    
# class House(Accomodation):
#     raise NotImplementedError


# class SharedAccomodation(Accomodation):
#     """Room inside a shared house"""
#     raise NotImplementedError

    
# class SharedRoom(Accomodation):
#     """Room in which several persons live"""
#     raise NotImplementedError
            
