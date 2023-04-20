#!/usr/bin/python3
"""contains the review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    product_id = ""  # will be the Product.id
    user_id = ""  # will be the User.id
    text = ""
