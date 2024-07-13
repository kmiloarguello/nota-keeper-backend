from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Note:
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
