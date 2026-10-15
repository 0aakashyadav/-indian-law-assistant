"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name, description="A source-grounded Indian legal-information assistant. Not a lawyer and not a substitute for professional legal advice.", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_origins, allow_credentials=False, allow_methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])
app.include_router(health_router, prefix="/api/v1")

@app.get("/", tags=["meta"])
def root() -> dict[str, str]:
    return {"name": settings.app_name, "status": "foundation", "disclaimer": "General legal information only; not legal advice.", "docs": "/docs"}
