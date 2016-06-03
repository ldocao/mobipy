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

        if isinstance(other, Money):
            if self.currency == other.currency:
                sum_value = self.value + other.value
                return self.__class__(sum_value, self.currency)
            else:
                sum_value_in_euro = self.value_in_euro() + other.value_in_euro()
                return self.__class__(sum_value_in_euro, EURO)
        else:
            raise TypeError("Can only add two Money instances.")

    def value_in_euro(self):
        return self.value * self.currency.unit_value_in_euro

    
    def __mul__(self, other):
        import utils
        
        if utils.is_numeric(other):
            return self.__class__(self.value*other, self.currency)
        else:
            raise TypeError("Can only multiply Money by a numerical variable.")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            same_value = self.value == other.value
            same_currency = self.currency == other.currency
            return same_value & same_currency
        else:
            raise TypeError("Cannot compare two different classes.")
        
    def __radd__(self, other):
        return self.__add__(other)
    

    def __rmul__(self, other):
        return self.__mul__(other)

    
    def __repr__(self):
        return str(self.value) + " " + str(self.currency)




    


