# -*- coding: utf-8 -*-

__all__ = ["Apartment", "House"]

import numpy as np
import pandas as pd
from mobipy.domain.accomodation.property.address import (Address,
                                                         LocationInBuilding,
                                                         Floor, Door)


class Property(object):
    DESCRIPTION_FILE = "./property.xlsx"
    ADDRESS = pd.read_excel(DESCRIPTION_FILE,
                            sheetname="address")
    LOCATION_IN_BUILDING = pd.read_excel(DESCRIPTION_FILE,
                                         sheetname="location_in_building")
    
    def __init__(self, _id):
        self._id = _id
        self.recover_attributes_from_excel() #name and address


        
    def recover_attributes_from_excel(self):
        name = self.recover_name()
        address = self.recover_address()
        setattr(self, "name", name)
        setattr(self, "address", address)
        return None

    
    def recover_name(self):
        selected_property = self._select_property()
        return self.get_attribute(selected_property, "name")

    
    def recover_address(self):
        selected_property = self._select_property()
        street = self.get_attribute(selected_property, "street")
        zipcode = selected_property["zipcode"]
        city = selected_property["city"]
        country = selected_property["country"]
        location_id = selected_property["location_in_building"]
        location = self._reconstruct_location_in_building(location_id)

        return Address(street, zipcode, city, country,
                       location_in_building=location)


    def _select_property(self):
        address = self.__class__.ADDRESS
        selected_property = address[address.id == self._id]
        return selected_property

    
    def _reconstruct_location_in_building(self, _id):
        print(_id)
        if np.isnan(_id):
            return np.nan
        else:
            all_locations = self.__class__.LOCATION_IN_BUILDING
            location = all_locations[all_locations["id"] == _id]
            floor = location["floor"]
            door = location["door"]
            return LocationInBuilding(Floor(floor), Door(door))
        
    
    @staticmethod
    def get_attribute(row, column_name):
        return row[column_name].values[0]


    
    def __repr__(self):
        return self.name




class Apartment(Property):
    def __init__(self, _id):
        super().__init__(_id)
        self.check_address()


    def check_address(self):
        if pd.isnull(self.address.location_in_building):
            error_message = "You must specify LocationInBuilding for Apartment"
            raise AttributeError(error_message)




class House(Property):
    pass
