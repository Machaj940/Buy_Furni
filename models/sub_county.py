#!/usr/bin/python3
"""contains the sub-county class"""


from models.base_model import BaseModel


class SubCounty(BaseModel):
    """sub-county class"""
    county_id = ""    # it will be the County.id
    name = ""
