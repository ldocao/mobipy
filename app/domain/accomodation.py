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




class Address():
    def __init__(self, number, road, postal_code, city, country):
        self.number = number
        self.road = road
        self.postal_code = postal_code
        self.city = city
        self.country = country



    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        if number <= 0:
            raise ValueError("Number should be > 0")
        else:
            self.__number = number



    

    
# class House(Accomodation):
#     raise NotImplementedError


# class SharedAccomodation(Accomodation):
#     """Room inside a shared house"""
#     raise NotImplementedError

    
# class SharedRoom(Accomodation):
#     """Room in which several persons live"""
#     raise NotImplementedError
            
