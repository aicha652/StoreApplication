from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv
from datetime import datetime

class Product(BaseModel, Base):
    __tablename__ = "products"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(80), nullable=False)
        price = Column(Numeric(10,2), nullable=False)
        stock = Column(Integer, nullable=False)
        desc = Column(Text, nullable=False)
        pub_date = Column(DateTime, nullable=False,default=datetime.now())
        category_id = Column(Integer, ForeignKey('category.id'),nullable=False)
        category = relationship('Category' , cascade="all_delete", backref="products")
        image_1 = Column(String(256), nullable=False, default='image1.jpg')
    else:
        name = ''
        price = ''
        stock = ''
        desc = ''
        pub_date = ''
        category_id = ''
        image = '' 
    def __repr__(self):
        return '<Product %r>' % self.name


class Category(BaseModel, Base):
    __tablename__ = "categories"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(64), nullable=False, unique=True)
    else:
        name = ''