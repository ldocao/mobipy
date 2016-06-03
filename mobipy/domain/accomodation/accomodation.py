# -*- coding: utf-8 -*-

from abc import ABCMeta


class Accomodation(metaclass=ABCMeta):
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


    


class Address():
    def __init__(self, street, postal_code, city, country):
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.country = country
