# MicroLoan - Complete Configuration & Deployment Guide

## Files You Need to Know About

### Entry Point Files

**`RUN_APP.bat`** ⭐ **Use this to start everything**
- Activates Python environment
- Installs dependencies
- Initializes database
- Starts backend server
- Opens frontend in browser
- **Best for:** First-time setup and daily use

**`START_BACKEND.bat`**
- Quick start for backend only (assumes dependencies installed)
- **Best for:** Development

**`SETUP_DATABASE.bat`**
- Fresh database initialization
- **Best for:** Troubleshooting database issues

**`CLEANUP.bat`**
- Removes virtual environment and cache
- **Best for:** Cleaning up before reinstalling

### Configuration Files

**`.env`** (Required)
- Your Paystack API keys go here
- Database URL configuration
- Secret keys for authentication
- **Create from:** `.env.example`

**`.env.example`** (Template)
- Shows what variables you need
- Copy and edit to create `.env`

### Documentation Files

**`README.md`**
- Quick start guide
- How to use the app
- Troubleshooting

**`SETUP.md`**
- Detailed installation steps
- Project structure
- API endpoints

**`PAYSTACK_SETUP.md`**
- M-Pesa integration guide
- Paystack account setup
- Payment testing

**`requirements.txt`** (in `backend/` folder)
- Python package list
- Auto-installed by RUN_APP.bat

---

## Step-by-Step Setup

### Scenario 1: Fresh Installation (Windows)

```bash
# Step 1: Navigate to project
cd "C:\Users\USER\3D Objects\project\Loans"

# Step 2: Copy example env file
copy .env.example .env

# Step 3: Edit .env with your Paystack keys
# Open .env in notepad and add:
# PAYSTACK_SECRET_KEY=sk_test_xxxxx
# PAYSTACK_PUBLIC_KEY=pk_test_xxxxx

# Step 4: Run the startup script
RUN_APP.bat

# Done! App opens automatically at http://localhost:8000
```

### Scenario 2: Already Have Dependencies Installed

```bash
cd "C:\Users\USER\3D Objects\project\Loans"

# Just start the backend
START_BACKEND.bat

# Or manually:
env\Scripts\activate
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

### Scenario 3: Database Issues (Reset Everything)

```bash
cd "C:\Users\USER\3D Objects\project\Loans"

# Clean up
CLEANUP.bat

# Fresh start
RUN_APP.bat
```

---

## Configuration Variables Explained

Create a `.env` file with these variables:

```env
# Database - SQLite for development
DATABASE_URL=sqlite:///./microloan.db

# Database - PostgreSQL for production
# DATABASE_URL=postgresql://user:password@host:5432/microloan

# Secret key for JWT tokens (CHANGE THIS!)
SECRET_KEY=your-super-secret-key-change-in-production-12345

# Paystack test keys (for development)
PAYSTACK_SECRET_KEY=sk_test_1234567890abcdefghijk
PAYSTACK_PUBLIC_KEY=pk_test_1234567890abcdefghijk

# Paystack live keys (for production)
# PAYSTACK_SECRET_KEY=sk_live_1234567890abcdefghijk
# PAYSTACK_PUBLIC_KEY=pk_live_1234567890abcdefghijk

# URLs (optional)
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
```

### Getting Paystack Keys

1. **Sign up:** https://paystack.com/signup
2. **Verify account:** Complete email/phone verification
3. **Go to Settings:** Click Settings ⚙️
4. **Get keys:** API Keys & Webhooks section
5. **Copy keys:** Secret and Public Key
6. **Paste in .env:** In `PAYSTACK_SECRET_KEY` and `PAYSTACK_PUBLIC_KEY`

---

## Project Architecture

### Backend (`backend/` folder)

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app setup
│   ├── models/
│   │   ├── user.py               # User database model
│   │   ├── loan.py               # Loan database model
│   │   └── transaction.py        # Transaction model
│   ├── routers/
│   │   ├── auth.py               # Login/Signup/Token endpoints
│   │   ├── loan.py               # Loan application endpoints
│   │   └── payments.py           # Payment initialization/verification
│   ├── schemas/
│   │   ├── user.py               # User request/response schemas
│   │   ├── loan.py               # Loan schemas
│   │   └── payment.py            # Payment schemas
│   ├── services/
│   │   └── paystack_service.py   # Paystack API integration
│   └── utils/
│       ├── auth.py               # JWT token handling
│       └── database.py           # Database connection
├── alembic/                        # Database migrations
├── requirements.txt               # Python dependencies
└── alembic.ini                    # Migration config
```

### Frontend (`frontend/` folder)

```
frontend/
├── index.html          # Home page / Landing page
├── login.html          # Login/Signup page
├── dashboard.html      # User dashboard with loans
├── loan_apply.html     # Loan application form
├── payment.html        # Payment processing page
├── scripts/
│   ├── api.js         # API client (all HTTP requests)
│   └── ui.js          # UI interactions (animations, etc.)
└── styles/
    ├── main.css       # Main stylesheet
    ├── glass.css      # Glass-morphism effects
    └── animations.css # Animations
```

### Root Level

```
Loans/
├── main.py            # WSGI entry point (serves frontend + backend)
├── init_db.py         # Database initialization script
├── .env               # Environment variables (CREATE THIS!)
├── .env.example       # Environment template
├── README.md          # Quick start guide
├── SETUP.md           # Detailed setup guide
├── PAYSTACK_SETUP.md  # Paystack integration guide
├── RUN_APP.bat        # Main startup script
├── START_BACKEND.bat  # Backend-only script
├── SETUP_DATABASE.bat # Database setup script
└── CLEANUP.bat        # Cleanup script
```

---

## API Documentation

### Base URL
```
http://localhost:8000
http://localhost:8000/api
```

### Interactive Docs
```
http://localhost:8000/docs (Swagger UI)
http://localhost:8000/redoc (ReDoc)
```

### Authentication Flow

1. **Register**
   ```
   POST /api/auth/register
   {
     "phone": "0712345678",
     "password": "securepassword"
   }
   Response:
   {
     "access_token": "eyJhbGc...",
     "refresh_token": "eyJhbGc...",
     "user": {
       "id": 1,
       "phone": "0712345678",
       "loan_limit": 5000
     }
   }
   ```

2. **Login**
   ```
   POST /api/auth/login
   {
     "phone": "0712345678",
     "password": "securepassword"
   }
   Response: Same as register
   ```

3. **Use Token**
   - Store `access_token` in `localStorage`
   - Send in every request: `Authorization: Bearer <token>`
   - Token expires in 30 minutes
   - Refresh with `refresh_token` when needed

### Loan Endpoints

```
GET /api/loans/history
  - Get all your loans
  - Required: Authorization header

POST /api/loans/apply
  Body: { "amount": 5000 }
  - Apply for new loan
  - Amount must be between 3000-60000
  - Can't have active loan (must repay first)

POST /api/loans/preview
  Body: { "principal": 5000 }
  - See fee calculation without applying
  - No auth required
```

### Payment Endpoints

```
POST /api/payments/initialize
  Body: { "loan_id": 1 }
  - Start payment process
  - Returns Paystack authorization URL
  - Redirect user to this URL

GET /api/payments/verify/{reference}
  - Verify payment after user returns
  - Check loan is marked as "repaid"

GET /api/payments/transactions
  - Get transaction history
  - Required: Authorization header
```

---

## Database Structure

### Users Table
```
id            INTEGER PRIMARY KEY
phone         VARCHAR UNIQUE
password_hash VARCHAR
loan_limit    INTEGER (starting 5000)
created_at    DATETIME
updated_at    DATETIME
```

### Loans Table
```
id          INTEGER PRIMARY KEY
user_id     FOREIGN KEY (users.id)
amount      INTEGER (principal amount)
fee         INTEGER (calculated fee)
total       INTEGER (amount + fee)
status      VARCHAR (pending/approved/repaid)
created_at  DATETIME
updated_at  DATETIME
```

### Transactions Table
```
id                   INTEGER PRIMARY KEY
loan_id              FOREIGN KEY (loans.id)
reference            VARCHAR (LOAN_1_ABC123)
amount               INTEGER
status               VARCHAR (pending/success/failed)
transaction_metadata VARCHAR (JSON with details)
created_at           DATETIME
updated_at           DATETIME
```

---

## Deployment Checklist

### Before Going Live

- [ ] Change `SECRET_KEY` to strong random string (use online generator)
- [ ] Get Paystack live keys (remove `_test_` prefix)
- [ ] Switch `DATABASE_URL` to PostgreSQL (not SQLite)
- [ ] Update `FRONTEND_URL` and `BACKEND_URL` to your domain
- [ ] Enable HTTPS (SSL certificate required)
- [ ] Test payment flow with live Paystack account
- [ ] Set up webhook URL in Paystack dashboard
- [ ] Configure banking/settlement details in Paystack
- [ ] Set up error logging/monitoring
- [ ] Create database backups
- [ ] Test on staging environment first

### Hosting Options

**Render.com** (Recommended)
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repo
4. Set environment variables
5. Deploy

**Heroku**
1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: python -m uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
   ```
3. Deploy:
   ```bash
   git push heroku main
   ```

**Railway/Fly.io/Others**
- Similar process
- Follow their specific documentation

### Environment Variables on Hosting

Set these on your hosting platform's dashboard:

```
DATABASE_URL=postgresql://...
SECRET_KEY=strong-random-string
PAYSTACK_SECRET_KEY=sk_live_...
PAYSTACK_PUBLIC_KEY=pk_live_...
FRONTEND_URL=https://your-domain.com
BACKEND_URL=https://your-domain.com
```

---

## Monitoring & Troubleshooting

### Check Application Health
```bash
# Check if backend is running
curl http://localhost:8000/health

# Should return:
# {"status": "healthy"}
```

### View Logs

**Backend Logs:**
- Check the terminal window running the backend
- Look for errors, warnings, or API calls

**Database Logs:**
- Check `microloan.db` exists
- Run `python init_db.py` if missing

**Frontend Errors:**
- Open browser DevTools (F12)
- Go to Console tab
- Look for red errors
- Check Network tab for failed API calls

### Common Issues

| Issue | Solution |
|-------|----------|
| "Port 8000 in use" | `netstat -ano \| findstr :8000` then kill process or use different port |
| "Module not found" | Run `pip install -r backend/requirements.txt` |
| "Database locked" | Delete `microloan.db` and run `python init_db.py` |
| "Payment fails" | Check Paystack keys, verify M-Pesa is enabled |
| "CORS errors" | Backend CORS is already wide open (allow all origins) |
| "Token expired" | Frontend auto-refreshes, clear localStorage if stuck |

---

## Security Best Practices

### Do's ✅
- Use strong `SECRET_KEY` (32+ characters, random)
- Keep `.env` file out of git (add to `.gitignore`)
- Use environment variables for all secrets
- Validate all user inputs
- Use HTTPS in production
- Hash passwords (already done with bcrypt)
- Update dependencies regularly
- Monitor transactions in Paystack dashboard

### Don'ts ❌
- Don't commit `.env` to git
- Don't expose SECRET_KEY in frontend
- Don't use weak passwords
- Don't store sensitive data in localStorage (only tokens)
- Don't skip HTTPS in production
- Don't log sensitive data
- Don't use SQL injection vulnerable queries (using ORM prevents this)
- Don't trust client-side validation only

---

## Performance Tips

### Optimize Database
- Index frequently queried columns
- Use pagination for large result sets
- Archive old transactions periodically

### Optimize Frontend
- Lazy load images
- Minify CSS/JS for production
- Use CDN for static files
- Enable browser caching

### Optimize Backend
- Use database connection pooling
- Implement caching for loan previews
- Add request rate limiting
- Monitor API response times

---

## Testing Checklist

### Unit Tests (Add in future)
- [ ] Test password hashing
- [ ] Test fee calculation logic
- [ ] Test JWT token generation

### Integration Tests (Add in future)
- [ ] Test auth flow (register → login → token)
- [ ] Test loan application flow
- [ ] Test payment initialization

### Manual Testing
- [ ] Register with phone number
- [ ] Login with correct credentials
- [ ] Apply for different loan amounts
- [ ] Check fee calculation accuracy
- [ ] Make payment via M-Pesa
- [ ] Verify payment completion
- [ ] Check loan marked as repaid
- [ ] Check loan limit increased
- [ ] Logout and re-login

### Edge Cases
- [ ] Try to apply with insufficient limit
- [ ] Try to apply when active loan exists
- [ ] Try invalid phone number format
- [ ] Try weak password
- [ ] Cancel payment mid-flow
- [ ] Payment timeout

---

## Support & Contact

### For Setup Help
1. Check `README.md` → Troubleshooting section
2. Check `SETUP.md` → Common Issues table
3. Check `PAYSTACK_SETUP.md` → FAQ section

### For Paystack Issues
- **Email:** support@paystack.com
- **Chat:** In Paystack dashboard
- **Docs:** https://paystack.com/docs

### For Code Issues
- Check backend logs in terminal
- Check frontend console (F12)
- Verify `.env` configuration
- Test API manually at `/docs` endpoint

---

**Ready to launch your MicroLoan app!** 🚀
