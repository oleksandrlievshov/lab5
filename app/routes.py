from fastapi import APIRouter, HTTPException, status
from app.schemas import Book, BookCreate
from app.database import book_collection
from bson import ObjectId

router = APIRouter()

def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "year": book["year"]
    }

@router.get("/", response_model=list[Book])
async def get_books():
    books = [book_helper(book) async for book in book_collection.find()]
    return books

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = await book_collection.find_one({"_id": ObjectId(book_id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_helper(book)

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    result = await book_collection.insert_one(book.dict())
    new_book = await book_collection.find_one({"_id": result.inserted_id})
    return book_helper(new_book)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str):
    result = await book_collection.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return
