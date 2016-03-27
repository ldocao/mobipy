# -*- coding: utf-8 -*-

from domain.money import Money





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



        
class TemporaryReccurence(object):
    """Recurrence limited in time"""
    def __init__(self, recurrence, time_range):
        self.recurrence = recurrence
        self.time_range = time_range

    
    
