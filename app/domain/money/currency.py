# -*- coding: utf-8 -*-


__all__ = ["EURO", "US_DOLLAR"]


class Currency(object):
    def __init__(self, symbol, unit_value_in_euro):
        self.symbol = symbol
        self.unit_value_in_euro = unit_value_in_euro


    def __eq__(self, other):
        if self.symbol == other.symbol:
            self.check_exchange_rate(other)
            return True
        else:
            return False


    def check_exchange_rate(self, other):
        return self.unit_value_in_euro == other.unit_value_in_euro

    
    def __repr__(self):
        return self.symbol


EURO = Currency("€", 1)
US_DOLLAR = Currency("USD", 0.9)



