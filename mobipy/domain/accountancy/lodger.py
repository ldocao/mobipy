# -*- coding: utf-8 -*-


__all__ = ["LodgerIdentity", "LodgerContract"]

import pandas as pd
from sqlalchemy import (Column,
                        Integer, String, Float, Date,
                        ForeignKey, CheckConstraint)
from mobipy.infrastructure.database.orm import Base
from mobipy.infrastructure.storage import LocalFile



    
class LodgerIdentity(Base):
    _FILE = LocalFile("mobipy/domain/accountancy/lodger.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="identity")
    
    _id = Column(Integer, primary_key=True, unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    mobile_phone = Column(String(20))
    home_phone = Column(String(20))
    email = Column(String(50))


class LodgerContract(Base):
    _FILE = LocalFile("mobipy/domain/accountancy/lodger.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="contract")

    _id = Column(Integer, primary_key=True, unique=True, nullable=False)
    rentable = Column(ForeignKey("rentable.name"), nullable=False)
    lodger = Column(ForeignKey("lodger.identity._id"), nullable=False)
    entry_date = Column(Date, nullable=False)
    exit_date = Column(Date)
    rent = Column(Float, nullable=False)
    expenditure = Column(Float, nullable=False)
    
    CheckConstraint("rent >= 0")
    CheckConstraint("expenditure >= 0")
