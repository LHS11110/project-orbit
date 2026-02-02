import './MovieCard.css';

function MovieCard({ movie, index }) {
    return (
        <article className="movie-card" style={{ animationDelay: `${index * 50}ms` }}>
            <div className="movie-card__poster">
                <img
                    src={movie.poster_url}
                    alt={movie.title}
                    className="movie-card__image"
                    loading="lazy"
                />
                <div className="movie-card__overlay">
                    <div className="movie-card__actions">
                        <button className="movie-card__btn movie-card__btn--play" aria-label="재생">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z" />
                            </svg>
                        </button>
                        <button className="movie-card__btn" aria-label="내 목록에 추가">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <line x1="12" y1="5" x2="12" y2="19" />
                                <line x1="5" y1="12" x2="19" y2="12" />
                            </svg>
                        </button>
                        <button className="movie-card__btn" aria-label="좋아요">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3" />
                            </svg>
                        </button>
                    </div>
                    <div className="movie-card__info">
                        <h3 className="movie-card__title">{movie.title}</h3>
                        <div className="movie-card__meta">
                            <span className="movie-card__rating">
                                <svg viewBox="0 0 24 24" fill="currentColor" width="12" height="12">
                                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                                </svg>
                                {movie.rating}
                            </span>
                            <span className="movie-card__year">{movie.year}</span>
                        </div>
                        <div className="movie-card__genres">
                            {movie.genre.slice(0, 2).map((g, i) => (
                                <span key={i} className="movie-card__genre">{g}</span>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </article>
    );
}

export default MovieCard;
