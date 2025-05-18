from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year: int = Field(..., ge=0, le=2100)

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: str
