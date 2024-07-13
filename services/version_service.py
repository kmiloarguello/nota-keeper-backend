from typing import List
from sqlalchemy.orm import Session
from models.version import Version

class VersionService:
    def __init__(self, db) -> None:
        self.db = db
        
    async def get_versions(self, note_id: int) -> List[Version]:
        with self.db() as session:
            versions = session.query(Version).filter(Version.note_id == note_id).all()
            return versions

    async def get_version(self, note_id: int, version_id: int) -> Version | None:
        with self.db() as session:
            version = session.query(Version).filter(Version.note_id == note_id, Version.version_id == version_id).first()
            return version
