import { useState, useEffect } from 'react';
import Hero from '../components/Hero';
import MovieRow from '../components/MovieRow';
import { getFeaturedMovie, getCategories } from '../api/movies';
import './Home.css';

function Home() {
    const [featuredMovie, setFeaturedMovie] = useState(null);
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function loadData() {
            try {
                setLoading(true);
                const [featured, cats] = await Promise.all([
                    getFeaturedMovie(),
                    getCategories()
                ]);
                setFeaturedMovie(featured);
                setCategories(cats);
            } catch (err) {
                console.error('Failed to load data:', err);
                setError('콘텐츠를 불러오는데 실패했습니다.');
            } finally {
                setLoading(false);
            }
        }
        loadData();
    }, []);

    if (error) {
        return (
            <div className="home__error">
                <div className="home__error-content">
                    <h2>😢 오류 발생</h2>
                    <p>{error}</p>
                    <p className="home__error-hint">백엔드 서버가 실행 중인지 확인해주세요.</p>
                    <button
                        className="btn btn-primary"
                        onClick={() => window.location.reload()}
                    >
                        다시 시도
                    </button>
                </div>
            </div>
        );
    }

    return (
        <main className="home">
            <Hero movie={featuredMovie} />

            <div className="home__content">
                {loading ? (
                    <div className="home__loading">
                        {[1, 2, 3].map(i => (
                            <div key={i} className="home__skeleton-row">
                                <div className="home__skeleton-title skeleton"></div>
                                <div className="home__skeleton-list">
                                    {[1, 2, 3, 4, 5, 6].map(j => (
                                        <div key={j} className="home__skeleton-card skeleton"></div>
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                ) : (
                    categories.map(category => (
                        <MovieRow
                            key={category.id}
                            title={category.name}
                            movies={category.movies}
                        />
                    ))
                )}
            </div>
        </main>
    );
}

export default Home;
