from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from sqlalchemy.orm import Session

from models import Movie, Category
import sql_models
from database import SessionLocal, engine

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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


FEATURED_MOVIE_ID = 7  # 듄: 파트 2


@app.get("/")
async def root():
    return {"message": "Welcome to Movie OTT API", "version": "1.0.0"}


@app.get("/api/movies", response_model=List[Movie])
async def get_movies(db: Session = Depends(get_db)):
    """전체 영화 목록 조회"""
    return db.query(sql_models.Movie).all()


@app.get("/api/movies/featured", response_model=Movie)
async def get_featured_movie(db: Session = Depends(get_db)):
    """추천 영화 조회"""
    movie = db.query(sql_models.Movie).filter(sql_models.Movie.id == FEATURED_MOVIE_ID).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Featured movie not found")
    return movie


@app.get("/api/movies/{movie_id}", response_model=Movie)
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """영화 상세 정보 조회"""
    movie = db.query(sql_models.Movie).filter(sql_models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.get("/api/categories", response_model=List[Category])
async def get_categories(db: Session = Depends(get_db)):
    """카테고리별 영화 목록 조회"""
    return db.query(sql_models.Category).all()


@app.get("/api/search")
async def search_movies(q: str, db: Session = Depends(get_db)):
    """영화 검색"""
    results = db.query(sql_models.Movie).filter(
        (sql_models.Movie.title.contains(q)) | (sql_models.Movie.description.contains(q))
    ).all()
    return results
