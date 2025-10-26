# src/api/routers/healthcheck.py
"""
Healthcheck Router
------------------
Provides /health endpoint to monitor API status.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    """Return API health status"""
    return {"status": "ok", "message": "API is running successfully"}
