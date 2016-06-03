# -*- coding: utf-8 -*-

import pytest
import domain.accomodation as accomodation


def test_incrementation_counter():
    apartment1 = accomodation.Apartment()
    apartment2 = accomodation.Apartment()
    assert apartment1._id == 1
    assert apartment2._id == 2
