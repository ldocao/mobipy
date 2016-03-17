# -*- coding: utf-8 -*-



class Metadata():
    def __init__(self, position):
        self.position = position



class Position():
    def __init__(self, address, location_in_building):
        self.address = address
        self.location_in_building = location_in_building


class LocationInBuilding():
    def __init__(self, floor, door):
        self.floor = floor
        self.door = door


class Floor():
    def __init__(self, number):
        self.number = number

    ##number may vary as function of country

    
class Door():
    def __init__(self, info):
        self.info = info #can store any kind of information



    
class Field():
    """Field on which the house is, if relevant"""
    def __init__(self, surface):
        self.surface = surface 


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

      

class Surface():
    def __init__(self, value, unit="square meter"):
        self.value = value
        self.unit = unit

    
