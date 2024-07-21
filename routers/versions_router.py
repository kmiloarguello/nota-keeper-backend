from fastapi import APIRouter, Depends, HTTPException, status
from models.version import Version
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.version_schema import VersionSchema, VersionOut
from services.version_service import VersionService

router = APIRouter(prefix="/notes/{note_id}/versions", tags=["Versions"])

@router.get("/", response_model=list[VersionOut])
def get_note_versions(note_id: int, db: Session = Depends(get_db)):
    versions = VersionService(db).get_versions(note_id)
    return versions

@router.get("/{version_id}", response_model=VersionOut)
def get_note_version(note_id: int, version_id: int, db: Session = Depends(get_db)):
    version = VersionService(db).get_version(note_id, version_id)
    if not version:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Version not found")
    return version
