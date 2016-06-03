# -*- coding: utf-8 -*-

import ipdb


class Transaction(object):
    """Abstract class"""
    def __init__(self, money, issuer, receiver):
        self.money = money
        self.issuer = issuer
        self.receiver = receiver

        
class UniqueTransaction(Transaction):
    """Unique (in time) Transaction"""
    def __init__(self, *args, date):
        super().__init__(args)
        self.date = date


class RecurrentTransaction(Transaction):
    """Recurrence limited in time"""
    def __init__(self, *args, recurrence):
        super().__init__(args)
        self.recurrence = recurrence





class TransactionFactory(object):
    """Abstract Factory for Transaction"""
    
    _type = {"unique" : UniqueTransaction,
             "recurrence" : RecurrentTransaction}


    @staticmethod
    def create_transaction(name, *args, **kwargs):
        transaction_class = TransactionFactory._type.get(name.lower(), None)
        return transaction_class(*args, **kwargs)
        








    


        
        
    
class Recurrence(object):
    """Transaction occuring regularly in time"""
    def __init__(self, transaction, frequency):
        self.transaction = transaction
        self.frequency = frequency
            
    
class Transaction(object):
    """Exchange of money between two entities"""
    def __init__(self, money, issuer, receiver):
        self.money = money
        self.issuer = issuer
        self.receiver = receiver

    def __repr__(self):
        import utils
        
        attributes = utils.get_attribute(self)
        arguments = [str(t[0])+"="+str(t[1]) for t in attributes]
        return self.__class__.__name__ + utils.parenthesis(arguments)




        


        

    
