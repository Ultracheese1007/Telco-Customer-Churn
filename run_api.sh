#!/bin/bash
echo "🚀 Starting FastAPI service..."
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
