#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.client import Client
from models.county import County
from models.furniture_type import FurnitureType
from models.product import Product
from models.review import Review
from models.sub_county import SubCounty
import os

classes = {"User": User, "BaseModel": BaseModel,
           "Client": Client, "County": County,
           "FurnitureType": FurnitureType, "Product": Product,
           "Review": Review, "SubCounty": SubCounty}

if os.getenv('BUY_FURNI_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
