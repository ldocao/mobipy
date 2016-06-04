# -*- coding: utf-8 -*-


__all__ = ["Base"]

import numpy as np
import ipdb
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from mobipy.infrastructure.setup import engine

@as_declarative()
class Base(object):
    """Augment the sqlalchemy Base class to dynamically define __tablename__ from the class name, and schema.

    Details
    -------
    http://stackoverflow.com/questions/19163911/dynamically-setting-tablename-for-sharding-in-sqlalchemy
    http://docs.sqlalchemy.org/en/rel_0_8/orm/extensions/declarative.html#augmenting-the-base

    """

    UNKNOWN = "NULL"

    def source_to_sql(self):
        df = self.SOURCE
        try:
            df.to_sql(self.__table__.fullname, engine,
                      if_exists="replace", index=False)
        except:
            raise ValueError("You cannot use if_exists='replace', when using to_sql because of ForeignKey constraint. Instead, load the Table from pandas.DataFrame only once, or use if_exists='append'.")
            
        return None

    
    #this function dynamically defines the table name as the class name
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    def __repr__(self):
        return str(self.__table__.__repr__())
