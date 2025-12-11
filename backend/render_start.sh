#!/bin/bash
set -e

echo "Running database migrations..."
cd /opt/render/project/src/backend
alembic upgrade head

echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT
