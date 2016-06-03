# -*- coding: utf-8 -*-

from abc import ABCMeta



class Address():
    def __init__(self, street, postal_code, city, country):
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.country = country

    

    
# class House(Accomodation):
#     raise NotImplementedError


# class SharedAccomodation(Accomodation):
#     """Room inside a shared house"""
#     raise NotImplementedError
