from typing import List
from models.user import User
from sqlalchemy.orm import Session
from schemas.user_schema import UserIn

class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_user(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.user_id == user_id).first()
      
    def create_user(self, user_data: UserIn) -> User:
        user = User(**user_data.model_dump())
        self.db.add(user)
        self.db.commit()
        return user
      
    @staticmethod
    async def get_current_user_id():
      pass
