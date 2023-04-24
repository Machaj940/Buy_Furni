#!/usr/bin/python3
"""Users are the sellers that list their products on Buy_Furni"""


from models.base_model import BaseModel


class User(BaseModel):
    """
        the User class
         - will add business_name attribute later. the console currently only
          takes one argument for certain functions eg Client.update(
          "<client id>, "business_name" "future Designs") will only
          register the name as future
    """
    #Business_name = ""
    email = ""
    password = ""
    phone_number = ""
