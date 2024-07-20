from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from config.db import engine, Base
from middlewares.error_handler import ErrorHandlerMiddleware
from routers.notes_router import router as notes_router
from routers.versions_router import router as versions_router
from routers.user_router import router as user_router
from models import *

Base.metadata.create_all(bind=engine)

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.title = "Nota keeper API"
app.version = "0.0.1"
app.description = "API for managing notes"

app.add_middleware(ErrorHandlerMiddleware)

@app.get("/")
async def root():
    return {"message": "Nota keeper API!"}

app.include_router(notes_router)
app.include_router(versions_router)
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
