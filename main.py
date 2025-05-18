from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as book_router

app = FastAPI(
    title="Library API with FastAPI and MongoDB"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/books", tags=["Books"])
