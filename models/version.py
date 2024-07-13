from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Version:
    __tablename__ = 'versions'
    
    id = Column(Integer, primary_key=True)
    version_id = Column(Integer)
    note_id = Column(Integer, ForeignKey('notes.note_id'))
    content = Column(String)
    created_at = Column(DateTime)