#!/usr/bin/python3
"""contains the sub-county class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class SubCounty(BaseModel, Base):
    """sub-county class to represent the sub-counties in Nairobi"""
    __tablename__ = "subcounties"
    county_id = Column(String(60), ForeignKey('counties.id'), nullable=False)
    name = Column(String(128), nullable=False)
