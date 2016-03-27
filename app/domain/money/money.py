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



class Transaction(Money):
    """Exchange of money between two entities"""
    pass





class Recurrence(object):
    """Transaction occuring regularly in time

    Parameters
    ----------
    transaction : Transaction

    frequency: Frequency
    """
    def __init__(self, transaction, frequency):
        self.transaction = transaction
        self.frequency = frequency




class TimeRange(object):
    """
    Parameters
    ----------
    start : DateTime

    end: DateTime
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TemporaryReccurence(object):
    """Recurrence limited in time"""
    def __init__(self, recurrence, time_range):
        self.recurrence = recurrence
        self.time_range = time_range

        


class Income(object):
    """

    Parameters
    ----------
    
    """
    def __init__(self, money, frequency):
        super().__init__(money.value, money.currency)
    
