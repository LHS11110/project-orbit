from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from models import Movie, Category
from data import MOVIES, CATEGORIES, FEATURED_MOVIE_ID

app = FastAPI(
    title="Movie OTT API",
    description="영화 스트리밍 OTT 플랫폼 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_movie_by_id(movie_id: int) -> Optional[dict]:
    """ID로 영화 찾기"""
    for movie in MOVIES:
        if movie["id"] == movie_id:
            return movie
    return None


@app.get("/")
async def root():
    return {"message": "Welcome to Movie OTT API", "version": "1.0.0"}


@app.get("/api/movies", response_model=List[Movie])
async def get_movies():
    """전체 영화 목록 조회"""
    return MOVIES


@app.get("/api/movies/featured", response_model=Movie)
async def get_featured_movie():
    """추천 영화 조회"""
    movie = get_movie_by_id(FEATURED_MOVIE_ID)
    if not movie:
        raise HTTPException(status_code=404, detail="Featured movie not found")
    return movie


@app.get("/api/movies/{movie_id}", response_model=Movie)
async def get_movie(movie_id: int):
    """영화 상세 정보 조회"""
    movie = get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.get("/api/categories", response_model=List[Category])
async def get_categories():
    """카테고리별 영화 목록 조회"""
    result = []
    for category in CATEGORIES:
        movies = []
        for movie_id in category["movie_ids"]:
            movie = get_movie_by_id(movie_id)
            if movie:
                movies.append(movie)
        result.append({
            "id": category["id"],
            "name": category["name"],
            "movies": movies
        })
    return result


@app.get("/api/search")
async def search_movies(q: str):
    """영화 검색"""
    query = q.lower()
    results = [
        movie for movie in MOVIES
        if query in movie["title"].lower() or query in movie["description"].lower()
    ]
    return results
