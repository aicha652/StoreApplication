#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.products import Product
from models.orders import Order
from models.cart import Cart
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Product": Product, "Order": Order, "Cart": Cart}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ECOMM_MYSQL_USER = getenv('ECOMM_MYSQL_USER')
        ECOMM_MYSQL_PWD = getenv('ECOMM_MYSQL_PWD')
        ECOMM_MYSQL_HOST = getenv('ECOMM_MYSQL_HOST')
        ECOMM_MYSQL_DB = getenv('ECOMM_MYSQL_DB')
        ECOMM_ENV = getenv('ECOMM_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ECOMM_MYSQL_USER,
                                             ECOMM_MYSQL_PWD,
                                             ECOMM_MYSQL_HOST,
                                             ECOMM_MYSQL_DB))
        if ECOMM_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """ retrieve one object """
        if cls in classes.values():
            obj = self.all(cls)
            for val in obj.values():
                if (val.id == id):
                    return val
        return None

    def count(self, cls=None):
        """ count num of obj in storage"""
        return len(self.all(cls))
