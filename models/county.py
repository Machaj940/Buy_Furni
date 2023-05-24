#!/usr/bin/python3
"""contains the county class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.sub_county import SubCounty


class County(BaseModel, Base):
    """class County - we"ll focus on Nairobi"""
    if os.getenv('BUY_FURNI_TYPE_STORAGE') == 'db':
        __tablename__ = "counties"
        name = Column(String(128), nullable=False)
        subcounties = relationship("SubCounty", backref="county",
                                   cascade="delete")

    else:
        name = ""

        @property
        def subcounties(self):
            subcounty_dict = models.storage.all(SubCounty)
            county_query = self.id
            subcounty_list = []
            for k, v in subcounty_dict.items():
                if v.county_id == self.id:
                    subcounty_list.append(v)
            return subcounty_list
