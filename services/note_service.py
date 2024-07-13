from typing import List
from models.note import Note
from schemas.note_schema import NoteIn, NoteUpdate

class NoteService:
    def __init__(self, db) -> None:
        self.db = db
        
    def get_notes(self) -> List[Note]:
        result = self.db.query(Note).all()
        return result
    
    def get_note(self, note_id: int) -> Note | None:
        return self.db.query(Note).filter(Note.id == note_id).first()

    def create_note(self, note_data: NoteIn) -> Note:
        note = Note(**note_data.model_dump())
        self.db.add(note)
        self.db.commit()
        return note

    def update_note(self, note_id: int, note_data: NoteUpdate) -> Note:
        note = self.db.query(Note).filter(Note.id == note_id).first()
        for field, value in note_data.model_dump():
            setattr(note, field, value)
        self.db.commit()
        self.db.refresh(note)
        return note

    def delete_note(self, note_id: int) -> None:
        note = self.db.query(Note).filter(Note.id == note_id).first()
        self.db.delete(note)
        self.db.commit()
