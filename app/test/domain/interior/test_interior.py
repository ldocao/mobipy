# -*- coding: utf-8 -*-

import pytest
import utils.geometry as geometry
from domain.interior.interior import Interior, Caracteristics, Surface
from domain.accomodation import Apartment
from domain.interior.room import Kitchen, MainRoom, Lavatory, LivingRoom, BedRoom


m2 = "square meter"

@pytest.fixture
def studio():
    studio = Caracteristics(Surface(geometry.Surface(30, m2)),
                            [Kitchen(Surface(geometry.Surface(10, m2))),
                             MainRoom(Surface(geometry.Surface(10, m2)))])
    return studio

@pytest.fixture
def room3():
    room3 =  Caracteristics(Surface(geometry.Surface(100, m2)),
                            [Kitchen(Surface(geometry.Surface(10, m2))),
                             MainRoom(Surface(geometry.Surface(10, m2))),
                             Lavatory(Surface(geometry.Surface(2, m2))),
                             LivingRoom(Surface(geometry.Surface(23, m2))),
                             BedRoom(Surface(geometry.Surface(23, m2)))])
    return room3

def test_number_of_habitable_room(studio):
    assert Caracteristics.number_of_habitable_room(studio) == 1

def test_number_of_habitable_room2(room3):
    assert Caracteristics.number_of_habitable_room(room3) == 3
