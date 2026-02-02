import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    const [scrolled, setScrolled] = useState(false);
    const [searchOpen, setSearchOpen] = useState(false);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 50);
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    return (
        <nav className={`navbar ${scrolled ? 'navbar--scrolled' : ''}`}>
            <div className="navbar__container">
                <div className="navbar__left">
                    <Link to="/" className="navbar__logo">
                        <span className="navbar__logo-icon">🎬</span>
                        <span className="navbar__logo-text">OrbitFlix</span>
                    </Link>

                    <ul className="navbar__menu">
                        <li><Link to="/" className="navbar__link navbar__link--active">홈</Link></li>
                        <li><Link to="/" className="navbar__link">영화</Link></li>
                        <li><Link to="/" className="navbar__link">TV 프로그램</Link></li>
                        <li><Link to="/" className="navbar__link">내가 찜한 콘텐츠</Link></li>
                    </ul>
                </div>

                <div className="navbar__right">
                    <div className={`navbar__search ${searchOpen ? 'navbar__search--open' : ''}`}>
                        <button
                            className="navbar__search-btn"
                            onClick={() => setSearchOpen(!searchOpen)}
                            aria-label="검색"
                        >
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <circle cx="11" cy="11" r="8" />
                                <path d="M21 21l-4.35-4.35" />
                            </svg>
                        </button>
                        <input
                            type="text"
                            className="navbar__search-input"
                            placeholder="제목, 장르..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                        />
                    </div>

                    <button className="navbar__icon-btn" aria-label="알림">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
                            <path d="M13.73 21a2 2 0 0 1-3.46 0" />
                        </svg>
                    </button>

                    <button className="navbar__profile">
                        <img
                            src="https://i.pravatar.cc/40?img=3"
                            alt="프로필"
                            className="navbar__profile-img"
                        />
                    </button>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
