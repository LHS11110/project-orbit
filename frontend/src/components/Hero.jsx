import './Hero.css';

function Hero({ movie }) {
    if (!movie) {
        return (
            <section className="hero hero--loading">
                <div className="hero__skeleton"></div>
            </section>
        );
    }

    return (
        <section className="hero">
            <div className="hero__backdrop">
                <img
                    src={movie.backdrop_url}
                    alt={movie.title}
                    className="hero__backdrop-img"
                />
                <div className="hero__gradient"></div>
            </div>

            <div className="hero__content">
                <div className="hero__badges">
                    <span className="hero__badge hero__badge--new">NEW</span>
                    <span className="hero__badge hero__badge--top">TOP 10</span>
                </div>

                <h1 className="hero__title">{movie.title}</h1>

                <div className="hero__meta">
                    <span className="hero__rating">
                        <svg viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                        </svg>
                        {movie.rating}
                    </span>
                    <span className="hero__year">{movie.year}</span>
                    <span className="hero__duration">{movie.duration}</span>
                    <span className="hero__genre">{movie.genre.join(' • ')}</span>
                </div>

                <p className="hero__description">{movie.description}</p>

                <div className="hero__actions">
                    <button className="hero__btn hero__btn--play">
                        <svg viewBox="0 0 24 24" fill="currentColor">
                            <path d="M8 5v14l11-7z" />
                        </svg>
                        재생
                    </button>
                    <button className="hero__btn hero__btn--info">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <circle cx="12" cy="12" r="10" />
                            <line x1="12" y1="16" x2="12" y2="12" />
                            <line x1="12" y1="8" x2="12.01" y2="8" />
                        </svg>
                        상세 정보
                    </button>
                    <button className="hero__btn hero__btn--add">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <line x1="12" y1="5" x2="12" y2="19" />
                            <line x1="5" y1="12" x2="19" y2="12" />
                        </svg>
                    </button>
                </div>
            </div>
        </section>
    );
}

export default Hero;
