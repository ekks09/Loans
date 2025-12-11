#!/usr/bin/env python
"""
MicroLoan Production Server
Optimized for Render deployment with Supabase PostgreSQL
"""
import os
import sys
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Set up event loop for Windows compatibility
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import auth, loan, payments

# Create FastAPI app
app = FastAPI(
    title="MicroLoan API",
    description="A microloan web application API with Paystack M-Pesa integration",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware - allow all origins for Render deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router)
app.include_router(loan.router)
app.include_router(payments.router)

# Mount static files
try:
    app.mount("/styles", StaticFiles(directory="frontend/styles"), name="styles")
    app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
except Exception as e:
    print(f"Warning: Could not mount static files: {e}")

# Frontend routes
@app.get("/", tags=["Frontend"])
async def serve_index():
    """Serve home page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {
        "message": "MicroLoan API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "status": "running"
    }

@app.get("/index.html", tags=["Frontend"])
async def serve_index_html():
    """Serve home page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"message": "Home Page"}

@app.get("/login.html", tags=["Frontend"])
async def serve_login():
    """Serve login page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "login.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"message": "Login Page"}

@app.get("/dashboard.html", tags=["Frontend"])
async def serve_dashboard():
    """Serve dashboard page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "dashboard.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"message": "Dashboard"}

@app.get("/loan_apply.html", tags=["Frontend"])
async def serve_loan_apply():
    """Serve loan application page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "loan_apply.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"message": "Loan Application"}

@app.get("/payment.html", tags=["Frontend"])
async def serve_payment():
    """Serve payment page"""
    file_path = os.path.join(os.path.dirname(__file__), "frontend", "payment.html")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"message": "Payment Page"}

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for Render"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "MicroLoan API"
    }

# API info endpoint
@app.get("/api", tags=["Info"])
async def api_info():
    """API information endpoint"""
    return {
        "name": "MicroLoan API",
        "version": "1.0.0",
        "description": "Microloan application with Paystack M-Pesa integration",
        "documentation": "/api/docs",
        "endpoints": {
            "auth": "/api/auth",
            "loans": "/api/loans",
            "payments": "/api/payments"
        }
    }

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 10000))
    host = "0.0.0.0"
    
    print("=" * 60)
    print("  MicroLoan Production Server (Render)")
    print("=" * 60)
    print(f"\nStarting server on {host}:{port}")
    print(f"Database: {os.getenv('DATABASE_URL', 'sqlite').split('@')[0]}")
    print(f"Frontend: http://0.0.0.0:{port}")
    print(f"API Docs: http://0.0.0.0:{port}/api/docs\n")
    
    # Initialize database on startup
    try:
        print("Initializing database...")
        sys.path.insert(0, os.path.dirname(__file__))
        from init_db import initialize_db
        initialize_db()
        print("✓ Database ready\n")
    except Exception as e:
        print(f"⚠ Database initialization warning: {e}\n")
    
    uvicorn.run(app, host=host, port=port, log_level="info")
