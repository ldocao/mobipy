# -*- coding: utf-8 -*-


import pytest
import utils.geometry as geometry

@pytest.fixture
def surface_meter():
    return geometry.Surface(1,"square meter")

@pytest.fixture
def surface_meter2():
    return geometry.Surface(2,"square meter")

@pytest.fixture
def surface_mile():
    return geometry.Surface(2,"square mile")

@pytest.fixture
def zero_surface():
    return geometry.Surface(0, "square meter")

def test_sum1(surface_meter, surface_meter2):
    total_surface = surface_meter + surface_meter2
    assert total_surface == geometry.Surface(3, "square meter")

    
def test_sum2(surface_meter, surface_meter2, zero_surface):
    total_surface = sum([surface_meter, surface_meter2], zero_surface)
    assert total_surface == geometry.Surface(3, "square meter")


def test_sum_error(surface_meter, surface_mile):
    with pytest.raises(TypeError):
        surface_meter + surface_mile

def test_comparison(surface_meter, surface_meter2):
    assert (surface_meter < surface_meter2) == True
    assert (surface_meter > surface_meter2) == False
