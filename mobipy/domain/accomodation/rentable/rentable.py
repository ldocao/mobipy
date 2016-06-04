# -*- coding: utf-8 -*-


__all__ = ["Solo", "Shared"]

import pandas as pd

from sqlalchemy import (Column, Integer, String, Float,
                        CheckConstraint, ForeignKey)

from mobipy.infrastructure.database.orm import Base
from mobipy.infrastructure.storage import LocalFile



    
class Solo(Base):
    _FILE = LocalFile("mobipy/domain/accomodation/rentable/rentable.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="solo")
    
    name = Column(String(50), primary_key=True, unique=True, nullable=False)
    property = Column(ForeignKey("property.name"), nullable=False)

    

class Shared(Base):
    _FILE = LocalFile("mobipy/domain/accomodation/rentable/rentable.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="shared")
    
    name = Column(String(50), primary_key=True, unique=True, nullable=False)
    property = Column(ForeignKey("property.name"), nullable=False)    
    personal_surface = Column(Float, nullable=False)
