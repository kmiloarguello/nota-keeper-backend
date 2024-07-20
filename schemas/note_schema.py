from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    id: Optional[int] = Field(None, title="Note ID", gt=0)
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=500)

class NoteIn(NoteBase):
    user_id: Optional[int] = None

class NoteOut(NoteBase):
    note_id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class NoteUpdate(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None
