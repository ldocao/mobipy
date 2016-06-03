# -*- coding: utf-8 -*-

import pytest
from domain.money.currency import EURO, US_DOLLAR
from domain.money import Money

@pytest.fixture
def bread():
    return Money(1.5, EURO)

@pytest.fixture
def butter():
    return Money(2, EURO)

@pytest.fixture
def coca_cola():
    return Money(2, US_DOLLAR)

@pytest.fixture
def orangina():
    return Money(3, US_DOLLAR)


def test_add1(bread, butter):
    french_items = bread + butter
    assert french_items.value == 3.5
    assert french_items.currency == EURO


def test_add2(coca_cola, orangina):
    american_items = coca_cola + orangina
    assert american_items.value == 5
    assert american_items.currency == US_DOLLAR
    
def test_add3(butter, coca_cola):
    mix_items = butter + coca_cola
    assert mix_items.value == butter.value + coca_cola.value*coca_cola.currency.unit_value_in_euro
    assert mix_items.currency == EURO
    

def test_add4(bread):
    with pytest.raises(TypeError):
        bread + 2

def test_add5(bread):
    with pytest.raises(TypeError):
        2 + bread


def test_eq1(bread, butter):
    is_equal = bread == butter
    assert is_equal == False

def test_eq2(bread):
    with pytest.raises(TypeError):
        bread == 2

def test_mul1(bread):
    assert bread*2 == Money(bread.value*2, EURO)

def test_mul2(bread):
    assert 2*bread == Money(bread.value*2, EURO)
