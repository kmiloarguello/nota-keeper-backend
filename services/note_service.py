from models.note import Note
from schemas.note_schema import NoteIn, NoteUpdate

class NoteService:
    async def get_note(self, note_id: int) -> Note | None:
        return note

    async def create_note(self, note_data: NoteIn, user_id: int) -> Note:
        return note

    async def update_note(self, note_id: int, note_data: NoteUpdate) -> Note:
        return note

    async def delete_note(self, note_id: int) -> None:
        pass
