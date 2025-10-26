# src/api/routers/healthcheck.py
"""
Healthcheck Router
------------------
Provides /health and /healthcheck endpoints to monitor API status.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    """Return API health status"""
    return {"status": "ok", "message": "API is running successfully"}

@router.get("/healthcheck")
def legacy_health():
    """Compatibility endpoint for CI/CD health checks"""
    return {"status": "ok", "message": "Legacy healthcheck for CI/CD compatibility"}
