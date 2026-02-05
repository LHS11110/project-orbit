from sqlalchemy.orm import Session
from database import SessionLocal, engine
import sql_models
import json

def seed_data():
    db = SessionLocal()
    
    # Ensure tables exist
    sql_models.Base.metadata.create_all(bind=engine)
    
    print("Cleaning up existing data...")
    # Delete all existing data
    db.query(sql_models.movie_category_association).delete()
    db.query(sql_models.Movie).delete()
    db.query(sql_models.Category).delete()
    db.commit()

    print("Seeding new data...")

    # Create Categories
    action = sql_models.Category(name="Action")
    scifi = sql_models.Category(name="Sci-Fi")
    drama = sql_models.Category(name="Drama")
    adventure = sql_models.Category(name="Adventure")
    fantasy = sql_models.Category(name="Fantasy")
    crime = sql_models.Category(name="Crime")
    animation = sql_models.Category(name="Animation")
    romance = sql_models.Category(name="Romance")
    thriller = sql_models.Category(name="Thriller")

    db.add_all([action, scifi, drama, adventure, fantasy, crime, animation, romance, thriller])
    db.commit()

    categories = {
        "Action": action, "Sci-Fi": scifi, "Drama": drama, "Adventure": adventure, 
        "Fantasy": fantasy, "Crime": crime, "Animation": animation, 
        "Romance": romance, "Thriller": thriller
    }

    movies_data = [
        {
            "id": 7, # Featured Movie
            "title": "Dune: Part Two",
            "description": "Paul Atreides unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family.",
            "poster_url": "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/xOMo8BRK7PfcJv9JCnx7s5hj0PX.jpg",
            "rating": 8.8,
            "year": 2024,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "duration": "2h 46m",
            "trailer_url": "https://www.youtube.com/embed/Way9Dexny3w",
            "categories": ["Action", "Adventure", "Sci-Fi"]
        },
        {
            "title": "Interstellar",
            "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/gDN2NWtHbs8ZWEBQM8Dh5OVXdb4.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
            "rating": 8.6,
            "year": 2014,
            "genre": ["Adventure", "Drama", "Sci-Fi"],
            "duration": "2h 49m",
            "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E",
            "categories": ["Adventure", "Drama", "Sci-Fi"]
        },
        {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/atSxEGstxXRoSKDQFBgqQ5lpGSt.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/s3TBrRGB1jav7nRDC1BdAJhunOV.jpg",
            "rating": 8.8,
            "year": 2010,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "duration": "2h 28m",
            "trailer_url": "https://www.youtube.com/embed/YoHD9XEInc0",
            "categories": ["Action", "Adventure", "Sci-Fi"]
        },
        {
            "title": "The Dark Knight",
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
            "rating": 9.0,
            "year": 2008,
            "genre": ["Action", "Crime", "Drama"],
            "duration": "2h 32m",
            "trailer_url": "https://www.youtube.com/embed/EXeTwQWrcwY",
            "categories": ["Action", "Crime", "Drama"]
        },
        {
            "title": "Avatar: The Way of Water",
            "description": "Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.",
            "poster_url": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/s16H6tpK2utvwDtzZ8Qy4qm5Emw.jpg",
            "rating": 7.7,
            "year": 2022,
            "genre": ["Sci-Fi", "Adventure", "Action"],
            "duration": "3h 12m",
            "trailer_url": "https://www.youtube.com/embed/d9MyqFCDqJQ",
            "categories": ["Sci-Fi", "Adventure", "Action"]
        },
        {
            "title": "The Matrix",
            "description": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/fxBxoXFAYKWde6lKzXxSusn18Av.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/ncEsesgOJ6rXOsLoQiwNOMEIZpz.jpg",
            "rating": 8.7,
            "year": 1999,
            "genre": ["Action", "Sci-Fi"],
            "duration": "2h 16m",
            "trailer_url": "https://www.youtube.com/embed/m8e-FF8MsqU",
            "categories": ["Action", "Sci-Fi"]
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "description": "Miles Morales is juggling his life between being a high school student and being a spider-man. When Wilson \"Kingpin\" Fisk uses a super collider, others from across the Spider-Verse are transported to this dimension.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/d9V6Q9vpVpmaca7vwSUbCajtDb3.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/qUv51IFUvVRAP237p14DPLkdura.jpg",
            "rating": 8.4,
            "year": 2018,
            "genre": ["Action", "Adventure", "Animation"],
            "duration": "1h 57m",
            "trailer_url": "https://www.youtube.com/embed/g4Hbz2jLxvQ",
            "categories": ["Action", "Adventure", "Animation"]
        },
        {
            "title": "Avengers: Endgame",
            "description": "After the devastating events of Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/z7ilT5rNN9kDo8JZmgyhM6ej2xv.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg",
            "rating": 8.3,
            "year": 2019,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "duration": "3h 1m",
            "trailer_url": "https://www.youtube.com/embed/TcMBFSGVi1c",
            "categories": ["Action", "Adventure", "Sci-Fi"]
        },
        {
            "title": "The Shawshank Redemption",
            "description": "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/qV9BQZdiM8foEzDz0Ag5hGWE5qM.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/kXfqcd0tIuWP0WgGD2l82tfYIkn.jpg",
            "rating": 8.7,
            "year": 1994,
            "genre": ["Drama", "Crime"],
            "duration": "2h 22m",
            "trailer_url": "https://www.youtube.com/embed/6hB3S9bIaco",
            "categories": ["Drama", "Crime"]
        },
        {
            "title": "Pulp Fiction",
            "description": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/6lXRHGoEbnnBUKsuqpL9JxD4DzT.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/suaEOtk1916guXlVTybVStSeRmZ.jpg",
            "rating": 8.5,
            "year": 1994,
            "genre": ["Thriller", "Crime"],
            "duration": "2h 34m",
            "trailer_url": "https://www.youtube.com/embed/s7EdQ4FqbhY",
            "categories": ["Thriller", "Crime"]
        },
        {
            "title": "Parasite",
            "description": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/eJ0kCMcqKLBUaHhB9PfOMFu2uim.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/hiKmpZMGZsrkA3cdce8a7Dpos1j.jpg",
            "rating": 8.5,
            "year": 2019,
            "genre": ["Comedy", "Thriller", "Drama"],
            "duration": "2h 12m",
            "trailer_url": "https://www.youtube.com/embed/5xH0HfJHsaY",
            "categories": ["Thriller", "Drama"]
        },
         {
            "title": "Your Name.",
            "description": "High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki’s body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.",
            "poster_url": "https://www.themoviedb.org/t/p/w1280/2DJCufz3Oa703PbLjNX1pM6MCG2.jpg",
            "backdrop_url": "https://image.tmdb.org/t/p/original/dIWwZW7dJJtqC6CgWzYkNVKIUm8.jpg",
            "rating": 8.5,
            "year": 2016,
            "genre": ["Romance", "Animation", "Drama"],
            "duration": "1h 46m",
            "trailer_url": "https://www.youtube.com/embed/a4ZNpNzdBl0",
            "categories": ["Romance", "Animation", "Drama"]
        }
    ]

    for movie_data in movies_data:
        movie = sql_models.Movie(
            id=movie_data.get("id"),
            title=movie_data["title"],
            description=movie_data["description"],
            poster_url=movie_data["poster_url"],
            backdrop_url=movie_data["backdrop_url"],
            rating=movie_data["rating"],
            year=movie_data["year"],
            genre=movie_data["genre"],
            duration=movie_data["duration"],
            trailer_url=movie_data["trailer_url"]
        )
        movie.categories = [categories[c] for c in movie_data["categories"] if c in categories]
        db.add(movie)

    db.commit()
    db.close()
    print("Database re-seeded successfully!")

if __name__ == "__main__":
    seed_data()
