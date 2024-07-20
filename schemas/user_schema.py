from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    id: Optional[int] = Field(None, title="Note ID", gt=0)
    username: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=1, max_length=100)
    password: str = Field(min_length=1, max_length=100)
    
class UserIn(UserBase):
    role: Optional[int] = None
    
class UserOut(UserBase):
    created_at: datetime
    updated_at: datetime
    role: Optional[int] = None
    class Config:
        orm_mode = True