from fastapi import APIRouter, Depends, HTTPException, status
from models.note import Note
from schemas.note_schema import NoteIn, NoteOut, NoteUpdate
from services.note_service import NoteService
from services.user_service import UserService

router = APIRouter(prefix="/notes", tags=["Notes"])
note_service = NoteService()

@router.get("/{note_id}", response_model=NoteOut)
async def get_note(note_id: int):
    note = await note_service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
async def create_note(note_data: NoteIn, current_user_id: int = Depends(UserService.get_current_user_id)):
    return await note_service.create_note(note_data, current_user_id)

@router.put("/{note_id}", response_model=NoteOut)
async def update_note(note_id: int, note_data: NoteUpdate):
    return await note_service.update_note(note_id, note_data)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    await note_service.delete_note(note_id)
