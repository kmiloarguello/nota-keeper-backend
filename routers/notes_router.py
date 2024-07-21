import json
from typing import  List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.note import Note
from schemas.note_schema import NoteIn, NoteOut, NoteUpdate
from schemas.version_schema import VersionIn
from services.note_service import NoteService
from services.user_service import UserService
from services.version_service import VersionService
from config.db import SessionLocal, get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/", response_model=List[NoteOut])
def get_notes(db: Session = Depends(get_db)) -> List[NoteOut]:
    notes = NoteService(db).get_notes()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(notes))

@router.get("/versions/{version_id}", response_model=NoteOut)
def get_note_by_version(version_id: int, db: Session = Depends(get_db)):
    note = NoteService(db).get_note_by_version(version_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = NoteService(db).get_note(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note_data: NoteIn, db: Session = Depends(get_db)):
    note = NoteService(db).create_note(note_data)
    data = {
        "content": note_data.content,
        "note_id": note.id
    }
    new_version_data = VersionIn(**data)
    VersionService(db).create_version(note.id, new_version_data)
    return note

@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_data: NoteUpdate, db: Session = Depends(get_db)):
    if not NoteService(db).get_note(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    data = {
        "content": note_data.content,
        "note_id": note_id
    }
    new_version = VersionIn(**data)
    VersionService(db).create_version(note_id, new_version)
    return NoteService(db).update_note(note_id, note_data)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    if not NoteService(db).get_note(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    if not VersionService(db).get_versions(note_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note has no versions")
    VersionService(db).delete_versions_by_note(note_id)
    NoteService(db).delete_note(note_id)
