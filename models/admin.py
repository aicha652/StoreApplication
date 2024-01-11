from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv

class User(BaseModel, Base):
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(80), unique=True, nullable=False)
        username = Column(String(80), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        password = Column(String(180), unique=False, nullable=False)
    else:
        name = ''
        username = ''
        email = ''
        password = ''
    def __repr__(self):
        return '<User %r>' % self.username