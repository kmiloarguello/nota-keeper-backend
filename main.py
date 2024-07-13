from fastapi import FastAPI, Depends
from config.db import engine, Base
from middlewares.error_handler import ErrorHandlerMiddleware
from routers.notes_router import router as notes_router
from routers.versions_router import router as versions_router

app = FastAPI()
app.title = "Nota keeper API"
app.version = "0.0.1"
app.description = "API for managing notes"

app.add_middleware(ErrorHandlerMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(notes_router)
# app.include_router(versions_router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
