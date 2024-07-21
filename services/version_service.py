from typing import List
from sqlalchemy.orm import Session
from models.version import Version
from schemas.version_schema import VersionIn, VersionOut

class VersionService:
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_versions(self, note_id: int) -> List[Version]:
        return self.db.query(Version).filter(Version.note_id == note_id).all()
    
    def get_version(self, note_id: int, version_id: int) -> Version | None:
        return self.db.query(Version).filter(Version.note_id == note_id, Version.id == version_id).first()
    
    def create_version(self, note_id: int, version_data: VersionIn) -> Version:
        # Extract data and add note_id
        version_info = version_data.model_dump()
        version_info['note_id'] = note_id  # Assuming 'note_id' is the correct field name in the Version model
        
        # Create Version object with note_id included
        version = Version(**version_info)
        self.db.add(version)
        self.db.commit()
        return version
    
    def delete_versions_by_note(self, note_id: int) -> None:
        self.db.query(Version).filter(Version.note_id == note_id).delete()
        self.db.commit()
