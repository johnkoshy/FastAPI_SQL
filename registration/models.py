from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
import datetime
  
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(150))
    email = Column(String(150))
    password = Column(String(150))
    phone = Column(Integer)
  
    def __repr__(self):
        return '<User %r>' % (self.id)  

