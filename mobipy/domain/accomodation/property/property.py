# -*- coding: utf-8 -*-

__all__ = ["Apartment", "House"]

from abc import ABCMeta


class Property(metaclass=ABCMeta):
    counter = 0
    
    def __init__(self, address):
        self._id = self.create_unique_id()
        self.address = address

        
    @classmethod
    def create_unique_id(cls):
        cls.counter += 1
        return cls.counter
    
    def __repr__(self):
        _id = str(self._id)
        return self.__class__.__name__ +"("+_id+")"




class Apartment(Property):
    def __init__(self, address):
        super().__init__(address)
        self.check_address()


    def check_address(self):
        if self.address.location_in_building is None:
            error_message = "You must specify LocationInBuilding for Apartment"
            raise AttributeError(error_message)




class House(Property):
    pass
