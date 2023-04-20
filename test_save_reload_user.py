#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.client import Client
from models.county import County
from models.furniture_type import FurnitureType
from models.product import Product
from models.review import Review
from models.sub_county import SubCounty

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Client --")
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

print("-- Create a county --")
my_county = County()
my_county.name = "Nairobi"
my_county.save()
print(my_county)

print("-- Create a furniture type --")
my_furni_type = FurnitureType()
my_furni_type.name = "Beds"
my_furni_type.save()
print(my_furni_type)

print("-- Create a product --")
my_product = Product()
my_product.name = "L-seat"
my_product.price = 500
my_product.save()
print(my_product)

print("-- Create a review --")
my_review = Review()
my_review.text = "Very comfortable"
my_review.save()
print(my_review)

print("-- Create a sub-county --")
my_sub_county = SubCounty()
my_sub_county.name = "Dagoretti"
my_sub_county.save()
print(my_sub_county)
