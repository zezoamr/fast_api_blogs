from sqlalchemy import Boolean, ForeignKey, String, Column, Integer
from sqlalchemy.orm import relationship
from blog.database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    pagenumber = Column(Integer)
    title = Column(String)
    publipshed = Column(Boolean)
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    creator = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    
    blogs = relationship("Blog", back_populates="creator")