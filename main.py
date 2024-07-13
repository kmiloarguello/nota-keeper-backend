from fastapi import FastAPI
from routers.notes_router import router as notes_router
from routers.versions_router import router as versions_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(notes_router)
app.include_router(versions_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
