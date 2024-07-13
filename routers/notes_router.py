from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.note import Note
from typing import  List
from schemas.note_schema import NoteIn, NoteOut, NoteUpdate
from services.note_service import NoteService
from services.user_service import UserService
from config.db import Session

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/", response_model=List[NoteOut])
def get_notes() -> List[NoteOut]:
    db = Session()
    result = NoteService(db).get_notes()
    print("result", result)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    db = Session()
    note_service = NoteService(db)
    note = note_service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note_data: NoteIn):
    db = Session()
    note_service = NoteService(db)
    return note_service.create_note(note_data)

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_data: NoteUpdate):
    db = Session()
    note_service = NoteService(db)
    return note_service.update_note(note_id, note_data)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    db = Session()
    note_service = NoteService(db)
    note_service.delete_note(note_id)
