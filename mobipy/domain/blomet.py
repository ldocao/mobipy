# -*- coding: utf-8 -*-

from domain.accomodation import Apartment, Address
from domain.apartment.metadata import (Metadata,
                                       Position,
                                       LocationInBuilding,
                                       Floor,
                                       Door)
from domain.interior.interior import Interior, Caracteristics, Surface, Equipment
from domain.interior.room import MainRoom, Kitchen, BathRoom

## define metadata
blomet = Apartment()
address = Address("56 rue Blomet", "75015", "Paris", "France")
location = LocationInBuilding(Floor(3), Door("gauche"))
position = Position(address, location)
blomet.metadata = Metadata(position)



## define interior
rooms = [MainRoom(Surface(13)), Kitchen(Surface(3)), BathRoom(Surface(2))]
caracteristics = Caracteristics(Surface(35.23, carrez=2), rooms)
equipment = Equipment()
blomet.interior = Interior(caracteristics, equipment)

