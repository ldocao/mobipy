# -*- coding: utf-8 -*-

from domain.accomodation import Apartment, Address
from domain.apartment.metadata import (Metadata,
                                       Position,
                                       LocationInBuilding,
                                       Floor,
                                       Door)


blomet = Apartment()
address = Address(56, "rue Blomet", "75015", "Paris", "France")
location = LocationInBuilding(Floor(3), Door("gauche"))
position = Position(address, location)
blomet.metadata = Metadata(position)

