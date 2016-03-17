# -*- coding: utf-8 -*-

import pytest
from domain.interior.interior import Interior, Caracteristics, Surface
from domain.accomodation import Apartment
from domain.interior.room import Kitchen, MainRoom, Lavatory, LivingRoom, BedRoom


@pytest.fixture
def studio():
    studio = Caracteristics(Surface(20),
                            [Kitchen(Surface(10)), MainRoom(Surface(10))])
    return studio

@pytest.fixture
def room3():
    room3 =  Caracteristics(Surface(20),
                            [Kitchen(Surface(10)), MainRoom(Surface(10)), Lavatory(Surface(2)), LivingRoom(Surface(23)), BedRoom(Surface(23))])
    return room3

def test_number_of_habitable_room(studio):
    assert Caracteristics.number_of_habitable_room(studio) == 1

def test_number_of_habitable_room2(room3):
    assert Caracteristics.number_of_habitable_room(room3) == 3
