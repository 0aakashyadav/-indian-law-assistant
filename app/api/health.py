"""Health and readiness endpoints."""
from fastapi import APIRouter
router = APIRouter(tags=["health"])

@router.get("/health", summary="Health check")
def health_check() -> dict[str, str]:
    """Process health only; does not imply legal data is loaded."""
    return {"status": "ok", "service": "indian-law-assistant"}
