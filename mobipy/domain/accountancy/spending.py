# -*- coding: utf-8 -*-


__all__ = ["FixedSpending", "RecurrencyType", "RecurrentSpending"]

import pandas as pd
from sqlalchemy import (Column,
                        Integer, Float, String, Date,
                        ForeignKey, CheckConstraint)
from mobipy.infrastructure.database.orm import Base
from mobipy.infrastructure.storage import LocalFile


class FixedSpending(Base):
    _FILE = LocalFile("mobipy/domain/accountancy/spending.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="fixed")
    
    _id = Column(Integer, primary_key=True, unique=True, nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)
    property = Column(ForeignKey("property.name"), nullable=False)
    label = Column(String(200))






class RecurrencyType(Base):
    _FILE = LocalFile("mobipy/domain/accountancy/spending.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="recurrency_type")
    
    name = Column(String(100), primary_key=True, unique=True, nullable=False)
    frequency = Column(String(50), nullable=False)


class RecurrentSpending(Base):
    _FILE = LocalFile("mobipy/domain/accountancy/spending.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="recurrency")
    
    _id = Column(Integer, primary_key=True, unique=True, nullable=False)
    value = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    type = Column(ForeignKey("recurrencytype.name"), nullable=False)




    
