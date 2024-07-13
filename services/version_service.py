from models.version import Version

class VersionService:
    async def get_versions(self, note_id: int) -> list[Version]:
        return versions

    async def get_version(self, note_id: int, version_id: int) -> Version | None:
        return version
