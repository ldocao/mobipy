# -*- coding: utf-8 -*-

class Money():
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            sum_value = self.value + other.value
            return Money(sum_value, self.currency)
        
