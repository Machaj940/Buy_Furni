#!/usr/bin/python3
"""Users are the sellers that list their products on Buy_Furni"""


from models.base_model import BaseModel


class User(BaseModel):
    """the User class"""
    Business_name = ""
    email = ""
    password = ""
    phone_number = ""
