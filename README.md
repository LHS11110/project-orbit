# 🎬 OrbitFlix

Netflix 스타일의 OTT 스트리밍 웹 서비스 클론 프로젝트입니다.

## ✨ 주요 기능

- **콘텐츠 탐색**: 영화/시리즈 검색, 필터링, 추천
- **상세 페이지**: 콘텐츠 정보 및 예고편 확인
- **반응형 UI**: 모든 디바이스에서 최적화된 경험

## 🛠️ 기술 스택

| Frontend | Backend |
|----------|---------|
| React + Vite | FastAPI (Python) |
| CSS3 | Uvicorn |

## 🚀 실행 방법

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📁 프로젝트 구조

```
project-orbit/
├── backend/          # FastAPI 서버
│   ├── main.py       # API 엔드포인트
│   ├── models.py     # 데이터 모델
│   └── data.py       # 샘플 데이터
├── frontend/         # React 클라이언트
│   └── src/
│       ├── components/
│       └── pages/
└── README.md
```

## 📝 License

MIT License
