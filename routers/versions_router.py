from fastapi import APIRouter, Depends, HTTPException, status
from models.version import Version
from schemas.version_schema import VersionSchema
from services.version_service import VersionService  # Replace with your service name

router = APIRouter(prefix="/notes/{note_id}/versions", tags=["Versions"])
version_service = VersionService()

@router.get("/", response_model=list[VersionSchema])
async def get_note_versions(note_id: int):
    versions = await version_service.get_versions(note_id)
    return versions

@router.get("/{version_id}", response_model=VersionSchema)
async def get_note_version(note_id: int, version_id: int):
    version = await version_service.get_version(note_id, version_id)
    if not version:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Version not found")
    return version
