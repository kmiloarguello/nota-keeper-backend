from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class User:
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)