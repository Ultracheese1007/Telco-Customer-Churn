# src/api/main.py
"""
FastAPI Application Entry Point
-------------------------------
This module initializes the FastAPI app, includes routers,
and serves as the main entry for running the API service.

Run with:
    uvicorn src.api.main:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import predict, healthcheck, data_preview


# ===============================================================
# Create FastAPI app
# ===============================================================
app = FastAPI(
    title="Telco Customer Churn Prediction API",
    description="Predict customer churn probability using trained ML models.",
    version="1.0.0"
)


# ===============================================================
# Allow local frontend or external tools (e.g., Streamlit, Postman)
# ===============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can restrict later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===============================================================
# Register routers
# ===============================================================
app.include_router(healthcheck.router, prefix="/api")
app.include_router(data_preview.router, prefix="/api")
app.include_router(predict.router, prefix="/api")


# ===============================================================
# Root endpoint
# ===============================================================
@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Telco Customer Churn API"}
