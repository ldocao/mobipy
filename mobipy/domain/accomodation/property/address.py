# -*- coding: utf-8 -*-

__all__ = ["Address", "LocationInBuilding", "Floor", "Door"]



class Address(object):
    def __init__(self,
                 street, zipcode, city, country,
                 location_in_building=None):
        """ 
        Parameters
        ----------
        street: String
        zipcode: String
        city: String
        country: String
        in_building: LocationInBuilding
        """
        self.street = street
        self.zipcode = zipcode
        self.city = city
        self.country = country
        self.location_in_building = location_in_building

    def __repr__(self):
        address_elements = [self.street,
                            self.zipcode,
                            self.city,
                            self.country,
                            str(self.location_in_building)]
        return ", ".join(address_elements)






        

class LocationInBuilding(object):
    def __init__(self, floor, door):
        self.floor = floor
        self.door = door

    def __repr__(self):
        floor = str(self.floor)
        door = str(self.door)
        return " ; ".join([floor, door])


class Floor(object):
    def __init__(self, number):
        self.number = number #may vary as function of country

    def __repr__(self):
        return "Floor: " + str(self.number)

    
class Door(object):
    def __init__(self, info):
        self.info = info #can store any kind of information

    def __repr__(self):
        return "Door: " + self.info
