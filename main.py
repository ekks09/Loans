import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.routers import auth, loan, payments

app = FastAPI(
    title="MicroLoan API",
    description="A microloan web application API with Paystack M-Pesa integration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(loan.router)
app.include_router(payments.router)

app.mount("/styles", StaticFiles(directory="frontend/styles"), name="styles")
app.mount("/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")

@app.get("/")
async def serve_index():
    return FileResponse("frontend/index.html")

@app.get("/index.html")
async def serve_index_html():
    return FileResponse("frontend/index.html")

@app.get("/login.html")
async def serve_login():
    return FileResponse("frontend/login.html")

@app.get("/dashboard.html")
async def serve_dashboard():
    return FileResponse("frontend/dashboard.html")

@app.get("/loan_apply.html")
async def serve_loan_apply():
    return FileResponse("frontend/loan_apply.html")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
