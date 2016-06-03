# -*- coding: utf-8 -*-

import pytest
from domain.money.currency import Currency


def test_equality1():
    EURO_1 = Currency("€", 1)
    EURO_2 = Currency("€", 1)
    assert EURO_1 == EURO_2


def test_equality2():
    EURO_1 = Currency("€", 1)
    EURO_2 = Currency("fake_euro", 1)
    assert EURO_1 != EURO_2

def test_equality3():
    EURO_1 = Currency("€", 1)
    EURO_2 = Currency("€", 2)
    with pytest.raises(ValueError):
        EURO_1 == EURO_2
