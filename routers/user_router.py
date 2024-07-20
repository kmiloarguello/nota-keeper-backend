from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import  List
from schemas.user_schema import UserIn, UserOut
from services.user_service import UserService
from config.db import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserIn, db: Session = Depends(get_db)):
    return UserService(db).create_user(user_data)
