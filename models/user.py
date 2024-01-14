#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Boolean, String
from flask_sqlalchemy import SQLAlchemy

class User(BaseModel, Base):
    if models.storage_t == 'db':
        __tablename__ = "users"
        username = Column(String(120), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        password = Column(String(120), unique=False, nullable=False)
        country = Column(String(120), unique=False, nullable=False)
        is_admin = Column(Boolean, nullable=False, default=False)
        address = Column(String(120), unique=False, nullable=False)
        phone = Column(String(120), unique=False, nullable=False)
    else:
        username = ""
        email = ""
        password = ""
        country = ""
        is_admin = ""
        address = ""
        phone = ""
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
