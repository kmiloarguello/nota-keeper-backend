from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.db import Base as Database

class User(Database):
  __tablename__ = 'users'
  
  id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
  )
  user_id = Column(Integer)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  role = Column(String)
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
  updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))