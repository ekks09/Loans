# MicroLoan Application - Setup & Installation Guide

## Quick Start

### Option 1: Automated Setup (Recommended - Windows)

Simply double-click `RUN_APP.bat` in the project folder. This will:
1. Create/activate Python virtual environment
2. Install all dependencies
3. Initialize the database
4. Start the backend server
5. Open the frontend in your browser

### Option 2: Manual Setup

#### Step 1: Configure Environment Variables

Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

Edit `.env` and add your **Paystack credentials**:
```
DATABASE_URL=sqlite:///./microloan.db
SECRET_KEY=your-super-secret-key-change-in-production
PAYSTACK_SECRET_KEY=sk_test_your_actual_secret_key
PAYSTACK_PUBLIC_KEY=pk_test_your_actual_public_key
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
```

#### Step 2: Get Paystack Credentials

1. Go to https://dashboard.paystack.com
2. Sign up or log in
3. Navigate to Settings > API Keys & Webhooks
4. Copy your **Secret Key** (starts with `sk_`) and **Public Key** (starts with `pk_`)
5. Paste them in your `.env` file

#### Step 3: Install Dependencies & Setup Database

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
env\Scripts\activate

# Install backend dependencies
cd backend
pip install -r requirements.txt
cd ..

# Initialize database
python init_db.py
```

#### Step 4: Run the Application

**Backend:**
```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:** Open your browser and go to:
```
http://localhost:8000
```

## Bat Files Available

### `RUN_APP.bat` (Main Entry Point)
Starts everything at once - database, backend, and opens frontend in browser.

### `START_BACKEND.bat`
Starts only the backend server for development.

### `SETUP_DATABASE.bat`
Re-initializes the database (clears all data).

## Project Structure

```
Loans/
├── backend/                    # FastAPI backend application
│   ├── app/
│   │   ├── models/            # Database models (User, Loan, Transaction)
│   │   ├── routers/           # API routes (auth, loans, payments)
│   │   ├── schemas/           # Request/response schemas
│   │   ├── services/          # Business logic (Paystack integration)
│   │   └── utils/             # Database, authentication utilities
│   ├── requirements.txt       # Python dependencies
│   └── alembic/               # Database migrations
├── frontend/                   # HTML/CSS/JS frontend
│   ├── index.html             # Home page
│   ├── login.html             # Login/Signup page
│   ├── dashboard.html         # User dashboard
│   ├── loan_apply.html        # Loan application page
│   ├── scripts/               # JavaScript files
│   └── styles/                # CSS stylesheets
├── .env                        # Environment variables (create from .env.example)
├── main.py                     # WSGI entry point
├── init_db.py                  # Database initialization script
└── RUN_APP.bat                 # Main startup script
```

## Features Implemented

### Authentication
- User registration with phone number and password
- Secure login with JWT tokens
- Token refresh mechanism
- Password hashing with bcrypt

### Loan Management
- Loan preview with automatic fee calculation
- Loan application with borrowing limits
- Loan history tracking
- Different loan tiers (3,000 - 60,000 KES)

### Payment Integration
- **Paystack Integration** with M-Pesa support
- Payment initialization with phone number
- Payment verification and webhook handling
- Transaction tracking and history
- Automatic loan limit increase after repayment

### Frontend
- Modern glass-morphism UI
- Responsive design
- Form validation
- Real-time loan calculations
- Error handling and user feedback

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh access token
- `GET /api/auth/me` - Get current user info

### Loans
- `POST /api/loans/preview` - Preview loan with fees
- `POST /api/loans/apply` - Apply for a loan
- `GET /api/loans/history` - Get user's loan history
- `GET /api/loans/{id}` - Get specific loan details

### Payments
- `POST /api/payments/initialize` - Initialize payment via Paystack
- `GET /api/payments/verify/{reference}` - Verify payment completion
- `POST /api/payments/webhook` - Paystack webhook handler
- `GET /api/payments/transactions` - Get transaction history

## Paystack M-Pesa Setup

### What is M-Pesa?

M-Pesa is a mobile money service in Kenya that allows payments via phone. Paystack acts as the intermediary.

### Setup Steps

1. **Get Paystack Account**
   - Visit https://paystack.com
   - Sign up and complete verification
   - Enable M-Pesa in your dashboard

2. **Configure Your Till Number**
   - In Paystack Dashboard: Settings → Payment Options → Mobile Money
   - Select Kenya and enable M-Pesa
   - Set your till number (Paystack will provide one or you can use existing)

3. **Add API Keys to .env**
   ```
   PAYSTACK_SECRET_KEY=sk_test_xxx
   PAYSTACK_PUBLIC_KEY=pk_test_xxx
   ```

4. **Test Payment Flow**
   - Go to login page and create account
   - Apply for a loan
   - Click "Pay Now"
   - Select M-Pesa and enter your phone number
   - You'll receive M-Pesa prompt on your phone
   - Enter M-Pesa PIN to complete payment

### Webhook Configuration

To receive payment notifications in your app:

1. Go to Paystack Dashboard
2. Settings → API Keys & Webhooks
3. Add Webhook URL: `http://your-domain/api/payments/webhook`
4. The app will automatically handle payment confirmations

## Troubleshooting

### "Cannot connect to server" error
- Make sure backend is running on port 8000
- Check if `.env` file exists
- Verify DATABASE_URL in `.env`

### "Payment initialization failed" error
- Verify Paystack API keys in `.env`
- Check if your Paystack account is live (not test mode)
- Ensure M-Pesa is enabled for your Paystack account

### Database errors
- Delete any existing database: `rm microloan.db` (or delete file in Windows)
- Run: `python init_db.py`
- This will create fresh tables

### Import errors when running backend
- Make sure virtual environment is activated: `env\Scripts\activate`
- Reinstall dependencies: `pip install -r backend/requirements.txt`

## Development Tips

### Testing the Frontend
- Open browser DevTools (F12)
- Go to Application/Storage tab
- Check `localStorage` for stored tokens
- Use Network tab to monitor API calls

### Testing Payments
- Use Paystack's test M-Pesa number for testing
- Contact Paystack support for test phone numbers
- Check Paystack dashboard transaction history for settlement

### Database Inspection
- The SQLite database is stored in `microloan.db`
- Use any SQLite viewer to inspect tables
- Or use Python: `sqlite3 microloan.db`

## Production Deployment

Before deploying to production:

1. **Change SECRET_KEY** in `.env` to a strong random string
2. **Use PostgreSQL** instead of SQLite:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/microloan
   ```
3. **Update PAYSTACK_SECRET_KEY** to your live key (remove `_test_`)
4. **Enable HTTPS** for your domain
5. **Update CORS origins** in `backend/app/main.py` to your domain
6. **Set up environment variables** on your hosting platform
7. **Run migrations**: `alembic upgrade head`

## Support & Issues

For issues or questions:
1. Check `.env` file configuration
2. Review browser console for frontend errors
3. Check backend logs for server errors
4. Verify Paystack dashboard for payment status
5. Contact Paystack support for payment issues

---

**Version:** 1.0.0  
**Last Updated:** December 2024
