from datetime import datetime
from flask_login import UserMixin
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime

class RegisterModel(BaseModel, UserMixin):
    __tablename__ = 'clients'
    name = Column(String(64), unique=False)
    username = Column(String(64), unique=True)
    email = Column(String(64), unique=True)
    password = Column(String(128), unique=False)
    country = Column(String(50), unique=False)
    state = Column(String(50), unique=False)
    city = Column(String(50), unique=False)
    address = Column(String(256), unique=False)
    contact = Column(String(16), unique=False)
    profile_image = Column(String(128), unique=False, default='profile.jpg')
    date_created = Column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<Register %r>' % self.name