#!/usr/bin/python3
"""Class client represents the clients that subscribe to GLS"""


from models.base_model import BaseModel


class Client(BaseModel):
    """
        the User class
        - will add business_name attribute later. the console currently only
          takes one argument for certain functions eg Client.update(
          "<client id>, "business_name" "future Designs") will only
          register the name as future
    """
    first_name = ""
    last_name = ""
    business_name = ""
    email = ""
    password = ""
    phone_number = ""
    sub_county= ""
    area_and_street = ""
