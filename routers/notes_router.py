from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.note import Note
from typing import  List
from schemas.note_schema import NoteIn, NoteOut, NoteUpdate
from services.note_service import NoteService
from services.user_service import UserService
from config.db import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/", response_model=List[NoteOut])
def get_notes(db: Session = Depends(get_db)) -> List[NoteOut]:
    note_service = NoteService(db)
    notes = note_service.get_notes()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(notes))

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note_service = NoteService(db)
    note = note_service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note_data: NoteIn, db: Session = Depends(get_db)):
    note_service = NoteService(db)
    return note_service.create_note(note_data)

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_data: NoteUpdate, db: Session = Depends(get_db)):
    note_service = NoteService(db)
    if not note_service.get_note(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note_service.update_note(note_id, note_data)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_service = NoteService(db)
    if not note_service.get_note(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    note_service.delete_note(note_id)
