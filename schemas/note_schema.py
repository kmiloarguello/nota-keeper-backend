from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteIn(NoteBase):
    user_id: int

class NoteOut(NoteBase):
    note_id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

class NoteUpdate(NoteBase):
    # Optional fields for updating notes
    title: Optional[str] = None
    content: Optional[str] = None
