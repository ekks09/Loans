# MicroLoan Application

## Overview
A complete, production-ready microloan web application built with:
- **Backend**: FastAPI (Python)
- **Frontend**: HTML + CSS + Vanilla JavaScript with animated glassmorphism UI
- **Database**: PostgreSQL (Supabase-compatible)
- **Payments**: Paystack with M-Pesa integration
- **Hosting**: Render.com ready

## Project Structure
```
/
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── main.py          # FastAPI app
│   │   ├── routers/         # API routes (auth, loan, payments)
│   │   ├── models/          # SQLAlchemy models (user, loan, transaction)
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Paystack service
│   │   └── utils/           # Auth & database utilities
│   ├── alembic/             # Database migrations
│   ├── requirements.txt
│   └── README.md            # Detailed documentation
├── frontend/                 # Static HTML/CSS/JS frontend
│   ├── index.html           # Landing page
│   ├── login.html           # Login/signup page
│   ├── dashboard.html       # User dashboard
│   ├── loan_apply.html      # Loan application
│   ├── styles/              # CSS files (main, glass, animations)
│   └── scripts/             # JavaScript (api.js, ui.js)
├── infra/
│   └── render.yaml          # Render deployment config
├── main.py                  # Combined app entry point
├── init_db.py               # Database initialization
├── .env.example             # Environment template
└── postman_collection.json  # API collection
```

## Key Features
- JWT authentication with phone + password
- Loan limits starting at 5,000, increasing by 2,000 per successful repayment (max 60,000)
- Fixed processing fee structure:
  - 3,000 → 200
  - 5,000 → 350
  - 6,000-8,000 → 460
  - 10,000 → 1,000
  - 20,000 → 2,000
  - 30,000 → 3,000
  - 40,000 → 4,000
  - 50,000 → 5,000
  - 60,000 → 6,000
- Paystack M-Pesa payment integration
- Beautiful glassmorphic animated UI

## Recent Changes
- 2024-12-11: Initial project creation with full backend and frontend

## Environment Variables Required
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT signing key
- `PAYSTACK_SECRET_KEY`: Paystack API key

## Running the Application
The app runs on port 5000 using uvicorn:
```
uvicorn main:app --host 0.0.0.0 --port 5000
```

## API Documentation
Available at `/docs` when the server is running.
