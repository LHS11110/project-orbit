from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
from database import Base
import json

# Association table for Many-to-Many relationship between Movie and Category
movie_category_association = Table(
    'movie_category_association',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    poster_url = Column(String)
    backdrop_url = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    # Storing list of strings as JSON string for simplicity in SQLite
    _genre = Column("genre", String)
    duration = Column(String)
    trailer_url = Column(String, nullable=True)

    categories = relationship("Category", secondary=movie_category_association, back_populates="movies")

    @property
    def genre(self):
        if self._genre:
            return json.loads(self._genre)
        return []

    @genre.setter
    def genre(self, value):
        self._genre = json.dumps(value)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    movies = relationship("Movie", secondary=movie_category_association, back_populates="categories")
