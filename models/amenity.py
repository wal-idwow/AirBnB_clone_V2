#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    __tablename__ = 'amenity'
    name = ""
