# -*- coding: utf-8 -*-

def parenthesis(*args):
    """Return input as a string with parenthesis

    Parameters
    ----------
    args: any
    
    Returns
    -------
    result: string
    """
    middle = ", ".join([str(s) for s in args])
    return "(" + middle + ")"
