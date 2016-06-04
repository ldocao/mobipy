# -*- coding: utf-8 -*-

__all__ = ["Address", "Property"]


import pandas as pd
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date

from mobipy.infrastructure.database.orm import Base
from mobipy.infrastructure.storage import LocalFile





class Address(Base):
    _FILE = LocalFile("mobipy/domain/accomodation/property/property.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="address")
    
    _id = Column(Integer, primary_key=True, unique=True, nullable=False)
    street = Column(String(100), nullable=False)
    zipcode = Column(String(10), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    floor = Column(Integer)
    door = Column(String(50))


class Property(Base):
    _FILE = LocalFile("mobipy/domain/accomodation/property/property.xlsx")
    SOURCE = pd.read_excel(_FILE.path, sheetname="property")
    
    name = Column(String(50), primary_key=True, unique=True, nullable=False)
    address = Column(Integer, ForeignKey("address._id"))
    start_date = Column(Date, nullable=False)
    # land_surface = Column(Float, nullable=False)
    # habitable_surface = Column(Float, nullable=False)
    
