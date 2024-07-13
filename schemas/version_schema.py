from pydantic import BaseModel, Field
from datetime import datetime

class VersionSchema(BaseModel):
    version_id: int
    note_id: int
    content: str
    created_at: datetime
