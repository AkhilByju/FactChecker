from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ContraCheck API (minimal)")

# Allow Vite dev server by default; tighten later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "backend", "version": "0.0.1"}

@app.get("/api/version")
def version():
    return {"version": "0.0.1"}
