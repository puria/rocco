# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, Numeric, DateTime
#from sqlalchemy.orm import relation, backref

from datetime import datetime

from rocco.model import DeclarativeBase, metadata, DBSession

class Statistic(DeclarativeBase):
    __tablename__ = 'statistics'
    
    id = Column(Integer, primary_key=True)
    device_id = Column(Unicode, nullable=False)
    lat = Column(Numeric)
    lng = Column(Numeric)
    km = Column(Numeric)
    date = Column(DateTime, default=datetime.now())

