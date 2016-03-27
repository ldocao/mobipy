# -*- coding: utf-8 -*-


__all__ = ["EURO", "US_DOLLAR"]


class Currency(object):
    def __init__(self, symbol, unit_value_in_euro):
        self.symbol = symbol
        self.unit_value_in_euro = unit_value_in_euro

    def __repr__(self):
        return self.symbol


EURO = Currency("€", 1)
US_DOLLAR = Currency("USD", 0.9)



