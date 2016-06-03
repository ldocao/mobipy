# -*- coding: utf-8 -*-


__all__ = ["blomet"]


from mobipy.domain.accomodation.property.property import Apartment
from mobipy.domain.accomodation.property.address import Address, LocationInBuilding, Floor, Door


## shortcut
location_in_building = LocationInBuilding(Floor(3), Door("gauche"))
address = Address("56 rue Blomet", "75015", "Paris", "France",
                  location_in_building=location_in_building)

## declare the property
blomet = Apartment(address)
