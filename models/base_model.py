#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import os
from sqlalchemy import DATETIME, Column, String
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            storage.save()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key,datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

            if 'id' not in kwargs:
                setattr(self,'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        t = "%Y-%m-%dT%H:%M:%S.%f"
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(t)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(t)
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    # def delete(self, obj=None):
    #     """"""
        
