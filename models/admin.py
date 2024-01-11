from models.base_model import BaseModel, Base
from sqlalchemy import Column, Boolean, String
from os import getenv

class User(BaseModel, Base):
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(80), unique=True, nullable=False)
        username = Column(String(80), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        password = Column(String(180), unique=False, nullable=False)
        is_admin = Column(Boolean, default=False)
    else:
        name = ''
        username = ''
        email = ''
        password = ''
        is_admin = ''
    def __repr__(self):
        return '<User %r>' % self.username