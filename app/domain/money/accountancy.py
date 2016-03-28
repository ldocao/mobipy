# -*- coding: utf-8 -*-

class Accountancy(object):
    """List all money entries (income, expense)"""
    
    def __init__(self, entries):
        self.entries = entries
        self.incomes = self.regroup_incomes()
        self.expenses = self.regroup_expenses()

    def regroup_incomes():
        raise NotImplementedError

    def regroup_expenses():
        raise NotImplementedError
        
