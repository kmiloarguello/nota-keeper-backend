from pydantic import BaseModel, Field
from datetime import datetime

class VersionSchema(BaseModel):
    id: int
    note_id: int
    content: str
    created_at: datetime
