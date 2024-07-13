from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Note:
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
