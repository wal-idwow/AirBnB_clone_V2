#!/usr/bin/python3
"""New sqlalchemy engine"""


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.base_model import BaseModel

        objects = {}
        classes = [BaseModel]

        if cls:
            if type(cls) == str:
                cls = eval(cls)
            classes.append(cls)

        for c in classes:
            for obj in self.__session.query(c):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects"""
        import models
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker
                                 (bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.remove()
