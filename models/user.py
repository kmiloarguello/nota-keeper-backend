from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.db import Base as Database
class User(Database):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  role = Column(String)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)