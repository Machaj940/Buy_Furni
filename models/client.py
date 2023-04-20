#!/usr/bin/python3
"""Class client represents the clients that subscribe to GLS"""


from models.base_model import BaseModel


class Client(BaseModel):
    """the User class"""
    full_name = ""
    business_name = ""
    email = ""
    password = ""
    phone_number = ""
    sub_county= ""
    area_and_street = ""
