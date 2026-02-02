import { useRef, useState } from 'react';
import MovieCard from './MovieCard';
import './MovieRow.css';

function MovieRow({ title, movies }) {
    const rowRef = useRef(null);
    const [showLeftArrow, setShowLeftArrow] = useState(false);
    const [showRightArrow, setShowRightArrow] = useState(true);

    const handleScroll = () => {
        if (rowRef.current) {
            const { scrollLeft, scrollWidth, clientWidth } = rowRef.current;
            setShowLeftArrow(scrollLeft > 0);
            setShowRightArrow(scrollLeft + clientWidth < scrollWidth - 10);
        }
    };

    const scroll = (direction) => {
        if (rowRef.current) {
            const scrollAmount = direction === 'left' ? -600 : 600;
            rowRef.current.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    };

    return (
        <section className="movie-row">
            <div className="movie-row__header">
                <h2 className="movie-row__title">{title}</h2>
                <button className="movie-row__view-all">
                    모두 보기
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <path d="M9 18l6-6-6-6" />
                    </svg>
                </button>
            </div>

            <div className="movie-row__container">
                {showLeftArrow && (
                    <button
                        className="movie-row__arrow movie-row__arrow--left"
                        onClick={() => scroll('left')}
                        aria-label="이전"
                    >
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <path d="M15 18l-6-6 6-6" />
                        </svg>
                    </button>
                )}

                <div
                    className="movie-row__list"
                    ref={rowRef}
                    onScroll={handleScroll}
                >
                    {movies.map((movie, index) => (
                        <MovieCard key={movie.id} movie={movie} index={index} />
                    ))}
                </div>

                {showRightArrow && (
                    <button
                        className="movie-row__arrow movie-row__arrow--right"
                        onClick={() => scroll('right')}
                        aria-label="다음"
                    >
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <path d="M9 18l6-6-6-6" />
                        </svg>
                    </button>
                )}
            </div>
        </section>
    );
}

export default MovieRow;
