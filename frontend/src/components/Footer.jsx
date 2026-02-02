import './Footer.css';

function Footer() {
    return (
        <footer className="footer">
            <div className="footer__container">
                <div className="footer__top">
                    <div className="footer__brand">
                        <span className="footer__logo">🎬 OrbitFlix</span>
                        <p className="footer__tagline">무한한 영화의 세계로</p>
                    </div>

                    <div className="footer__links">
                        <div className="footer__column">
                            <h4>탐색</h4>
                            <ul>
                                <li><a href="#">홈</a></li>
                                <li><a href="#">영화</a></li>
                                <li><a href="#">TV 프로그램</a></li>
                                <li><a href="#">신규 콘텐츠</a></li>
                            </ul>
                        </div>
                        <div className="footer__column">
                            <h4>지원</h4>
                            <ul>
                                <li><a href="#">고객센터</a></li>
                                <li><a href="#">자주 묻는 질문</a></li>
                                <li><a href="#">기기 지원</a></li>
                                <li><a href="#">문의하기</a></li>
                            </ul>
                        </div>
                        <div className="footer__column">
                            <h4>법적 고지</h4>
                            <ul>
                                <li><a href="#">이용약관</a></li>
                                <li><a href="#">개인정보처리방침</a></li>
                                <li><a href="#">쿠키 설정</a></li>
                                <li><a href="#">저작권 정보</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div className="footer__bottom">
                    <div className="footer__social">
                        <a href="#" aria-label="Instagram">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5" fill="none" stroke="currentColor" strokeWidth="2" />
                                <circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" strokeWidth="2" />
                                <circle cx="18" cy="6" r="1.5" />
                            </svg>
                        </a>
                        <a href="#" aria-label="Twitter">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z" fill="none" stroke="currentColor" strokeWidth="2" />
                            </svg>
                        </a>
                        <a href="#" aria-label="YouTube">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z" fill="none" stroke="currentColor" strokeWidth="2" />
                                <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" />
                            </svg>
                        </a>
                    </div>
                    <p className="footer__copyright">© 2026 OrbitFlix. All rights reserved.</p>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
