from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    id: int
    title: str
    description: str
    poster_url: str
    backdrop_url: str
    rating: float
    year: int
    genre: List[str]
    duration: str
    trailer_url: Optional[str] = None


class Category(BaseModel):
    id: int
    name: str
    movies: List[Movie]
