#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import models


class Order(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = "orders"
        quantity = Column(Integer, nullable=False)
        user_id = Column(String(60), ForeignKey("users.id", onupdate='CASCADE',ondelete='CASCADE'), nullable=False)
        product_id = Column(String(60), ForeignKey("products.id", onupdate='CASCADE',ondelete='CASCADE'), nullable=False)
    else:
        quantity = ""
        user_id = ""
        product_id = ""
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
