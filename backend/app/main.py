import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, loan, payments

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

@app.get("/")
async def root():
    return {"message": "MicroLoan API is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
