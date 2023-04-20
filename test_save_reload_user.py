#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.client import Client

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_client = Client()
my_client.full_name = "Betty"
my_client.business_name = "GLS"
my_client.email = "airbnb@mail.com"
my_client.password = "root"
my_client.save()
print(my_client)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
