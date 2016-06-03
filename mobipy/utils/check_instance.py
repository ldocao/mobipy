# -*- coding: utf-8 -*-

def is_positive_integer(x):
    if isinstance(x, int):
        return x >= 0
    else:
        return False

        
def is_numeric(x):
    if isinstance(x, bool):
        return False
    else:
        try:
            x+1
            return True
        except TypeError:
            return False
