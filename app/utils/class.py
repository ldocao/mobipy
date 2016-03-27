def get_attribute(instance):
    """Return all attributes of an instance (except all internal built-in)

    Parameters
    ----------
    instance: Object
        Object you want to inspect the attributes from


    Returns
    -------
    attributes: list of tuple
        list of attributes and associated values

    Example
    -------
    >>> a = TableField("username", "varchar", max_char=10)
    >>> get_attributes(a)
    >>> [("name", "username"), ("field_type", "varchar"), ("max_char", 10)]
    """
    
    attributes = inspect.getmembers(instance, lambda a:not(inspect.isroutine(a)))
    return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
