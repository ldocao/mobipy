# -*- coding: utf-8 -*-

from domain.money import Money





class Transaction(object):
    """Exchange of money between two entities"""
    def __init__(self, money, issuer, receiver):
        self.money = money
        self.issuer = issuer
        self.receiver = receiver





class TransactionFactory(object):
    """Abstract Factory for Transaction"""
    
    ## List all types of transaction
    _type = {"unique" : UniqueTransaction,
             "recurrence" : RecurrentTransaction}


    @staticmethod
    def get_transaction(name, *args, **kwargs):
        transaction_class = TransactionFactory._type.get(name.lower(),
                                                         default=None)
        return transaction_class(*args, **kwargs)
        

    

class UniqueTransaction(object):
    """Unique (in time) Transaction"""
    pass



class RecurrentTransaction(object):
    """Transaction occuring regularly in time"""




        
class TemporaryReccurence(object):
    """Recurrence limited in time"""
    def __init__(self, recurrence, time_range):
        self.recurrence = recurrence
        self.time_range = time_range

    
    
