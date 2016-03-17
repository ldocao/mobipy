# -*- coding: utf-8 -*-

import pytest
from domain.interior.interior import Interior, Caracteristics, Surface
from domain.accomodation import Apartment
from domain.interior.room import Kitchen, MainRoom


@pytest.fixture
def studio():
    studio = Caracteristics(Surface(20),
                            [Kitchen(Surface(10)), MainRoom(Surface(10))])
    return studio

def test_number_of_habitable_room(studio):
    assert Caracteristics.number_of_habitable_room(studio) == 1
