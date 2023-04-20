#!/usr/bin/python3
"""contains the sub-county class"""


from models.base_model import BaseModel


class SubCounty(BaseModel):
    """sub-county class to represent the sub-counties in Nairobi"""
    county_id = ""    # it will be the County.id
    name = ""
