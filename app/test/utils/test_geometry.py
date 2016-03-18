# -*- coding: utf-8 -*-


import pytest
from utils.geometry import GeometricalSurface

@pytest.fixture
def surface_meter():
    return GeometricalSurface(1,"square meter")

@pytest.fixture
def surface_meter2():
    return GeometricalSurface(2,"square meter")

@pytest.fixture
def surface_mile():
    return GeometricalSurface(2,"square mile")


def test_sum(surface_meter, surface_meter2):
    total_surface = surface_meter + surface_meter2
    assert total_surface == GeometricalSurface(3, "square meter")


def test_sum_error(surface_meter, surface_mile):
    with pytest.raises(TypeError):
        surface_meter + surface_mile
