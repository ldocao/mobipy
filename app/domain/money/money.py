# -*- coding: utf-8 -*-



class Money(object):
    """Value with associated currency

    Parameters
    ----------
    value: float

    currency: Currency
    """
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __add__(self, other):
        from domain.money.currency import EURO
        
        if self.currency == other.currency:
            sum_value = self.value + other.value
            return Money(sum_value, self.currency)
        else:
            sum_value_in_euro = self.value_in_euro() + other.value_in_euro()
            return Money(sum_value_in_euro, EURO)


    def value_in_euro(self):
        return self.value * self.currency.unit_value_in_euro


    def __repr__(self):
        return str(self.value) + " " + self.currency




    


