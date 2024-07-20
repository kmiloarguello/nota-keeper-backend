from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.db import Base as Database
class Version(Database):
    __tablename__ = 'versions'
    
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
    )
    note_id = Column(Integer, ForeignKey('notes.id'), nullable=False)
    content = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))