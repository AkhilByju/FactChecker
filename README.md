# ContraCheck — Minimal Starter

**Purpose:** tiny runnable skeleton with a React frontend and FastAPI backend.
No business logic — just health checks and a placeholder UI.

## Dev quickstart

Terminal 1:
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Terminal 2:
```bash
cd frontend
npm install
npm run dev
# open http://localhost:5173
```

## Docker (optional)
```bash
docker compose up --build
# frontend: http://localhost:5173
# backend:  http://localhost:8000/api/health
```

_Last generated 2025-08-20_
