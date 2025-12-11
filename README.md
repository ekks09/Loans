# MicroLoan Application - Complete Setup Guide

## Overview

MicroLoan is a FastAPI-based microloan application with:
- User authentication (register/login)
- Loan application with automatic fee calculation
- **Paystack M-Pesa integration** for payments
- Dashboard with loan management
- Mobile-responsive modern UI

## Quick Start (Windows)

### Step 1: Double-Click to Run
Simply double-click `RUN_APP.bat` in the project folder.

That's it! The script will:
✅ Create Python virtual environment  
✅ Install all dependencies  
✅ Initialize the database  
✅ Start the backend server  
✅ Open the frontend in your browser  

**Access the app at:** http://localhost:8000

---

## Detailed Setup (If Manual Setup Needed)

### Prerequisites
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Windows 10/11 or compatible OS
- A Paystack account ([Sign up free](https://paystack.com))

### Step 1: Configure Paystack (IMPORTANT)

**Get Your Paystack Credentials:**

1. Go to https://dashboard.paystack.com/signup
2. Complete account verification
3. Click your **Settings** ⚙️
4. Go to **API Keys & Webhooks**
5. Copy your **Secret Key** (starts with `sk_`)
6. Copy your **Public Key** (starts with `pk_`)

**Add Keys to .env File:**

1. Open `.env` file in the project root (or create from `.env.example`)
2. Paste your Paystack keys:

```env
DATABASE_URL=sqlite:///./microloan.db
SECRET_KEY=your-super-secret-key-change-in-production
PAYSTACK_SECRET_KEY=sk_test_your_actual_key_here
PAYSTACK_PUBLIC_KEY=pk_test_your_actual_key_here
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
```

### Step 2: Install & Initialize

**In PowerShell or Command Prompt:**

```bash
# Navigate to project folder
cd "C:\Users\USER\3D Objects\project\Loans"

# Create virtual environment
python -m venv env

# Activate it
env\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt
cd ..

# Initialize database
python init_db.py
```

### Step 3: Run the Application

**Terminal 1 - Start Backend:**
```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Open Frontend:**
```
http://localhost:8000
```

---

## Available Startup Scripts

### `RUN_APP.bat` ⭐ Main Script
Starts everything automatically. **Use this first!**

### `START_BACKEND.bat`
Starts only the backend server (useful for development).

### `SETUP_DATABASE.bat`
Re-initializes the database (wipes all data).

---

## Project Structure

```
Loans/
├── backend/
│   ├── app/
│   │   ├── models/           # User, Loan, Transaction models
│   │   ├── routers/          # API endpoints
│   │   ├── schemas/          # Request/response schemas
│   │   ├── services/         # Paystack service
│   │   └── utils/            # Auth, database utilities
│   ├── requirements.txt      # Python packages
│   └── alembic/              # Database migrations
├── frontend/
│   ├── index.html            # Home page
│   ├── login.html            # Login/Registration
│   ├── dashboard.html        # User dashboard
│   ├── loan_apply.html       # Loan application
│   ├── payment.html          # Payment page
│   ├── scripts/              # JavaScript files
│   └── styles/               # CSS styles
├── .env                      # Environment configuration
├── main.py                   # Entry point
├── init_db.py                # Database init script
└── RUN_APP.bat               # Main startup script
```

---

## How to Use the App

### 1. Register/Login
- Go to http://localhost:8000
- Create account with phone number & password
- Or login if already registered

### 2. Apply for Loan
- Click "Apply for Loan"
- Select loan amount (3,000 - 60,000 KES)
- System automatically calculates fees
- Click "Apply Now"
- Loan gets approved instantly

### 3. Make Payment (M-Pesa)
- Go to Dashboard
- Click "Pay Now" on your loan
- Enter your M-Pesa phone number
- Click "Proceed to Payment"
- You'll be redirected to Paystack
- Complete M-Pesa prompt on your phone
- Return to app for confirmation

---

## M-Pesa Setup with Paystack

### What is M-Pesa?
M-Pesa is a mobile money service in Kenya. Paystack handles the integration.

### Enable M-Pesa on Paystack

1. **Dashboard** → Settings → Payment Options
2. Select **Kenya** → Mobile Money
3. Enable **M-Pesa**
4. You'll get a Till Number (or use your existing one)
5. Set webhook URL: `http://your-domain/api/payments/webhook`

### Test M-Pesa Payment

1. Register account: Phone `0712345678`, Password `test123`
2. Apply for loan: Select any amount
3. Click "Pay Now"
4. Use test phone number Paystack provides
5. You'll get M-Pesa prompt on your test phone
6. Enter PIN to complete

### Live Deployment

To go live with real payments:

1. **Switch from test keys to live keys:**
   - Remove `_test_` from your Paystack keys
   - Use your production secret/public keys

2. **Update .env:**
   ```env
   PAYSTACK_SECRET_KEY=sk_live_actual_key
   PAYSTACK_PUBLIC_KEY=pk_live_actual_key
   ```

3. **Use real phone numbers** during testing

---

## API Endpoints Reference

### Authentication
```
POST   /api/auth/register      Register new user
POST   /api/auth/login          User login
POST   /api/auth/refresh        Refresh token
GET    /api/auth/me             Get current user
```

### Loans
```
POST   /api/loans/preview      Preview loan with fees
POST   /api/loans/apply         Apply for loan
GET    /api/loans/history       Get your loans
GET    /api/loans/{id}          Get loan details
```

### Payments
```
POST   /api/payments/initialize  Start payment
GET    /api/payments/verify/{ref} Verify payment
GET    /api/payments/transactions Get transaction history
POST   /api/payments/webhook     Paystack webhook
```

---

## Troubleshooting

### ❌ "Cannot connect to server"
- Check backend is running on port 8000
- Verify `.env` file exists
- Try: http://localhost:8000/docs (API docs)

### ❌ "Paystack payment failed"
- Verify API keys in `.env` are correct
- Check Paystack account is verified
- Ensure M-Pesa is enabled for your country
- Test with Paystack test number first

### ❌ "Login/Registration fails"
- Check database was initialized: `python init_db.py`
- Clear browser cache/cookies
- Check browser console (F12) for errors
- Verify phone number format (e.g., 0712345678)

### ❌ "Port 8000 already in use"
Open another port:
```bash
python -m uvicorn backend.app.main:app --port 8001
```

### ❌ "Module not found" errors
Reinstall dependencies:
```bash
pip install --upgrade -r backend/requirements.txt
```

---

## Database

### Location
`microloan.db` (SQLite database in project root)

### Reset Database
```bash
# Delete the database file and reinitialize
python init_db.py
```

### View Database (optional)
Download [DB Browser for SQLite](https://sqlitebrowser.org/) to inspect tables.

---

## Features

✅ User Authentication (JWT tokens)  
✅ Loan Application & Approval  
✅ Automatic Fee Calculation  
✅ Payment via Paystack M-Pesa  
✅ Webhook Payment Verification  
✅ Loan History Tracking  
✅ Responsive Design  
✅ Error Handling  
✅ Secure Password Storage  

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Backend won't start | Port 8000 in use. Kill process or use `--port 8001` |
| No database tables | Run `python init_db.py` |
| Login/Signup errors | Check backend logs. Verify .env file. |
| Payment not working | Verify Paystack keys. Check webhook. Test mode setup. |
| CORS errors | Backend CORS already enabled for all origins |
| Slow startup | First run downloads dependencies. Be patient. |

---

## Development Tips

### View Backend Logs
Check the backend terminal window for errors and API calls.

### View Frontend Errors
Press **F12** in browser → Console tab

### Test API Directly
Visit http://localhost:8000/docs for **Swagger API docs**

### Check Stored Data
Press **F12** → Application → LocalStorage → Check tokens

### Paystack Dashboard
- View live transactions at https://dashboard.paystack.com
- Check settlement account
- Download transaction reports

---

## Support & Next Steps

### For Issues:
1. Check the **Troubleshooting** section above
2. Review backend terminal logs
3. Check browser console (F12)
4. Verify Paystack account status
5. Contact Paystack support for payment issues

### To Customize:
- **Change fees:** Edit `backend/app/routers/loan.py` (FEE_STRUCTURE)
- **Change UI colors:** Edit `frontend/styles/main.css`
- **Add new features:** See `backend/app/routers/` for examples

### To Deploy:
- Use Render.com, Railway.app, or Heroku
- Update DATABASE_URL to PostgreSQL
- Set environment variables on hosting platform
- Update CORS origins to your domain

---

## Security Reminders

⚠️ **Before Production:**
- Change `SECRET_KEY` to strong random string
- Use PostgreSQL database (not SQLite)
- Switch Paystack keys from test to live
- Enable HTTPS on your domain
- Update CORS origins to your domain only
- Never commit `.env` file to git

---

## Version Info
- **Version:** 1.0.0
- **Backend:** FastAPI + SQLAlchemy
- **Frontend:** HTML/CSS/JavaScript
- **Payment:** Paystack M-Pesa
- **Database:** SQLite (dev) / PostgreSQL (production)

---

**Ready to go! Double-click `RUN_APP.bat` and start lending!** 🚀
