#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import models


class Product(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = "products"
        name = Column(String(80), nullable=False)
        price = Column(Integer, nullable=False, default=0)
        desc = Column(Text, nullable=False)
        image_1 = Column(String(256), nullable=False, default='image1.jpg')
    else:
        name = ''
        price = ''
        desc = ''
        image_1 = ''
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
