from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class VersionSchema(BaseModel):
    id: Optional[int] = Field(None, title="Note ID", gt=0)
    note_id: int = Field(..., title="Note ID", gt=0)
    
class VersionIn(VersionSchema):
    content: str = Field(min_length=1, max_length=500)
class VersionOut(VersionSchema):
    created_at: datetime
    content: str
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True