#!/usr/bin/python3
"""contains the product class that lists each product available"""


from models.base_model import BaseModel


class Product(BaseModel):
    """State class"""
    subcounty_id = ""  # will be the SubCounty.id
    user_id = ""  # will be the User.id
    name = ""
    description = ""
    price = 0
    furniture_type_ids = []  # will be a list of FurnitureType.id
