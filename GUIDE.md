╔════════════════════════════════════════════════════════════════════════════╗
║                          MICROLOAN APPLICATION                              ║
║                     Complete Setup & Deployment Guide                        ║
╚════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 PROJECT OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MicroLoan is a complete microloan application with:
  ✅ User authentication (register/login/JWT)
  ✅ Loan application with smart fee calculation
  ✅ Paystack M-Pesa payment integration (Kenya)
  ✅ Payment verification & settlement tracking
  ✅ Dashboard with loan management
  ✅ Modern responsive UI with glass-morphism design
  ✅ Production-ready error handling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ QUICKSTART (5 MINUTES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOR WINDOWS USERS:

  1. Create Paystack Account (free)
     → Go to https://paystack.com/signup
     → Verify email and phone
     → Complete business information

  2. Get Your API Keys
     → In Paystack Dashboard → Settings ⚙️
     → API Keys & Webhooks section
     → Copy "Secret Key" and "Public Key"

  3. Configure Your App
     → Edit .env file in project root
     → Paste your Paystack keys:
        PAYSTACK_SECRET_KEY=sk_test_xxxxx
        PAYSTACK_PUBLIC_KEY=pk_test_xxxxx

  4. Start Everything
     → Double-click RUN_APP.bat
     → App automatically opens at http://localhost:8000

  5. Test It
     → Register with phone number
     → Apply for loan
     → Click "Pay Now"
     → Complete test payment

✅ Done! Your app is running.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 WHAT YOU GET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Frontend Access:
  • Home Page:        http://localhost:8000
  • Login/Register:   http://localhost:8000/login.html
  • Dashboard:        http://localhost:8000/dashboard.html
  • Apply Loan:       http://localhost:8000/loan_apply.html
  • Payment:          http://localhost:8000/payment.html

Backend Access:
  • API Root:         http://localhost:8000/api
  • Swagger Docs:     http://localhost:8000/docs
  • ReDoc:            http://localhost:8000/redoc
  • Health Check:     http://localhost:8000/health

Database:
  • File:             microloan.db (SQLite)
  • Tables:           users, loans, transactions
  • Tool:             DB Browser for SQLite (optional)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 STARTUP SCRIPTS EXPLAINED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RUN_APP.bat  ⭐ USE THIS FIRST
  → Creates virtual environment
  → Installs all dependencies
  → Initializes database
  → Starts backend server
  → Opens frontend in browser
  → Perfect for: First time setup, daily use

START_BACKEND.bat
  → Quick backend startup (assumes dependencies installed)
  → Useful for: Development iteration
  → Command: env\Scripts\activate && python -m uvicorn ...

SETUP_DATABASE.bat
  → Fresh database initialization
  → Clears all existing data
  → Useful for: Troubleshooting, reset

CLEANUP.bat
  → Removes virtual environment
  → Clears Python cache files
  → Useful for: Before reinstalling, freeing space

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 IMPORTANT FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Documentation:
  • README.md              → Quick overview & how to use
  • SETUP.md               → Detailed installation steps
  • PAYSTACK_SETUP.md      → Paystack/M-Pesa integration guide
  • CONFIGURATION.md       → Full configuration reference
  • QUICK_REFERENCE.md     → Cheat sheet with quick tips

Configuration:
  • .env                   → Your API keys go here (CREATE THIS!)
  • .env.example           → Template (copy to .env and edit)

Code:
  • backend/app/          → FastAPI application
  • frontend/             → HTML/CSS/JavaScript
  • main.py               → Entry point
  • init_db.py            → Database initialization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ CONFIGURATION GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Create .env File
  → Copy .env.example to .env
  → Command: copy .env.example .env

Step 2: Get Paystack Keys
  → Sign up at https://paystack.com
  → Go to Settings → API Keys & Webhooks
  → Copy Secret Key and Public Key

Step 3: Edit .env
  PAYSTACK_SECRET_KEY=sk_test_your_secret_key
  PAYSTACK_PUBLIC_KEY=pk_test_your_public_key

Other .env Variables:
  DATABASE_URL=sqlite:///./microloan.db  # SQLite for dev
  SECRET_KEY=your-secret-key-here        # Change this!
  FRONTEND_URL=http://localhost:3000     # Frontend URL
  BACKEND_URL=http://localhost:8000      # Backend URL

Step 4: Validate Configuration
  → Run: python -m uvicorn backend.app.main:app --reload
  → Visit: http://localhost:8000/health
  → Should show: {"status": "healthy"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎬 APPLICATION FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User Journey:

  1. REGISTER/LOGIN
     • User enters phone number and password
     • System creates account or logs in
     • JWT token stored in browser

  2. APPLY FOR LOAN
     • User selects loan amount (3,000-60,000 KES)
     • System calculates fees automatically
     • Loan approved immediately
     • Shows in dashboard

  3. MAKE PAYMENT (M-Pesa)
     • User clicks "Pay Now" on loan
     • Enters M-Pesa phone number
     • Redirected to Paystack
     • M-Pesa prompt sent to phone
     • User enters PIN to confirm
     • Payment processed

  4. CONFIRMATION
     • App verifies payment with Paystack
     • Loan marked as "Repaid"
     • Loan limit increased for next loan
     • Transaction recorded

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 LOAN LIMITS & FEES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Amount    Fee      Total to Repay
3,000  →  200   =  3,200 KES
5,000  →  350   =  5,350 KES
10,000 →  1,000 =  11,000 KES
20,000 →  2,000 =  22,000 KES
30,000 →  3,000 =  33,000 KES
50,000 →  5,000 =  55,000 KES
60,000 →  6,000 =  66,000 KES

Starting Loan Limit:    5,000 KES
Maximum Loan Limit:     60,000 KES
Limit Increase:         +2,000 KES per repaid loan
Active Loans:           Only 1 at a time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔒 AUTHENTICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

JWT Token Authentication:
  • Access Token:   30 minutes validity
  • Refresh Token:  7 days validity
  • Stored In:      Browser localStorage
  • Sent As:        "Authorization: Bearer <token>"

Password Security:
  • Algorithm:      bcrypt
  • Salt Rounds:    12
  • Never stored:   Plain text passwords
  • Validation:     Using passlib library

Session Management:
  • Token Refresh:  Automatic when expired
  • Logout:         Clears localStorage
  • CORS:           Enabled for all origins (dev mode)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💳 PAYSTACK M-PESA INTEGRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What is M-Pesa?
  • Mobile money service by Safaricom (Kenya)
  • Works on any phone (basic or smartphone)
  • Users transfer money using PIN
  • Fastest payment method in Kenya

Paystack's Role:
  • Intermediary between your app and M-Pesa
  • Handles payment processing
  • Secure transaction processing
  • Webhook notifications
  • Settlement to your bank account

Integration Steps:
  1. User selects loan and clicks "Pay Now"
  2. App sends request to Paystack API
  3. Paystack returns authorization URL
  4. User redirected to Paystack payment page
  5. User enters M-Pesa phone number
  6. M-Pesa prompt sent to their phone
  7. User enters PIN to confirm
  8. Payment processed by Paystack
  9. App receives callback/webhook
  10. Loan marked as repaid
  11. Loan limit increased
  12. Settlement to your bank account (T+1 or as configured)

Test Flow:
  → Use Paystack test numbers
  → No real money transferred
  → Full flow simulation
  → Check Paystack dashboard for transactions

Live Flow:
  → Use live Paystack keys
  → Real payments processed
  → Real M-Pesa prompts sent
  → Real money settlement to bank

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 API ENDPOINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Authentication:
  POST   /api/auth/register      Register new user
  POST   /api/auth/login          Login with credentials
  POST   /api/auth/refresh        Refresh access token
  GET    /api/auth/me             Get current user info

Loans:
  POST   /api/loans/preview      Preview loan with calculated fees
  POST   /api/loans/apply         Apply for new loan
  GET    /api/loans/history       Get all your loans
  GET    /api/loans/{id}          Get specific loan details

Payments:
  POST   /api/payments/initialize  Initialize payment via Paystack
  GET    /api/payments/verify/{ref} Verify payment completion
  POST   /api/payments/webhook     Webhook for Paystack notifications
  GET    /api/payments/transactions Get transaction history

View Full Docs at: http://localhost:8000/docs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Backend Won't Start

  Error: "Address already in use :8000"
  → Solution: Port 8000 is taken by another process
  → Fix: netstat -ano | findstr :8000
         taskkill /PID <pid_number> /F
         Or: Use different port with --port 8001

  Error: "ModuleNotFoundError: No module named 'fastapi'"
  → Solution: Dependencies not installed
  → Fix: pip install -r backend/requirements.txt

Cannot Connect to Server

  Error: "Unable to connect to server"
  → Check: Backend is running (see terminal)
  → Check: .env file exists with API keys
  → Check: http://localhost:8000/health returns {"status": "healthy"}

Login/Registration Fails

  Error: "Loan application failed" or "Login failed"
  → Check: Backend logs in terminal for error message
  → Check: Phone number format (0712345678 - 10 digits)
  → Check: Database exists (microloan.db in project root)
  → Fix: Run python init_db.py to reinitialize

Payment Initialization Fails

  Error: "Transaction initialization failed"
  → Check: Paystack keys are correct in .env
  → Check: Keys have no extra spaces or special characters
  → Check: Paystack account is verified
  → Check: M-Pesa is enabled in Paystack Payment Options
  → Fix: Verify keys at https://dashboard.paystack.com

Payment Completes but App Shows Error

  Error: "Payment verification failed"
  → Cause: Webhook not properly configured
  → Check: Webhook URL in Paystack dashboard
  → Check: Backend is accessible from internet (if live)
  → Check: Backend logs for webhook errors

Database Errors

  Error: "Database locked" or "No such table"
  → Solution: Database corrupted or not initialized
  → Fix: Run SETUP_DATABASE.bat
  → Or: python init_db.py

CORS Errors in Browser Console

  Error: "Access to XMLHttpRequest blocked by CORS"
  → Status: CORS is already enabled for development
  → Check: No CORS errors should occur in dev mode
  → For production: Update CORS origins in backend/app/main.py

Frontend Not Loading

  Error: Page shows blank or 404 Not Found
  → Check: main.py exists and serves frontend files
  → Check: frontend/ folder and HTML files exist
  → Check: URL is http://localhost:8000 (not http://localhost:8000/api)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 MOVING TO PRODUCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-Production Checklist:

  [ ] Upgrade Paystack Account
      → Contact support@paystack.com
      → Complete KYC verification
      → Request live access

  [ ] Get Production Keys
      → Generate live keys (start with sk_live_)
      → Copy them safely
      → Never commit to git

  [ ] Update Environment Variables
      → Change PAYSTACK_SECRET_KEY to sk_live_...
      → Change PAYSTACK_PUBLIC_KEY to pk_live_...
      → Change SECRET_KEY to strong random string
      → Update DATABASE_URL to PostgreSQL

  [ ] Set Up Database
      → Use PostgreSQL (not SQLite)
      → Create backup procedures
      → Set up regular backups

  [ ] Configure Hosting
      → Choose: Render.com, Railway.app, Heroku, etc.
      → Set environment variables on platform
      → Deploy code
      → Test on staging first

  [ ] Set Up HTTPS/SSL
      → Get SSL certificate (free with Let's Encrypt)
      → Enable HTTPS on domain
      → Force HTTPS redirects

  [ ] Configure Paystack Webhook
      → Set webhook URL: https://your-domain.com/api/payments/webhook
      → Test webhook delivery
      → Monitor webhook logs

  [ ] Set Up Banking
      → Link bank account in Paystack
      → Set settlement schedule
      → Configure payout preferences

  [ ] Test Live Payments
      → Make test transaction with small amount
      → Verify payment appears in dashboard
      → Check bank account receives settlement

  [ ] Enable Monitoring
      → Set up error logging (Sentry, DataDog, etc.)
      → Monitor payment transactions
      → Set up alerts for failures

  [ ] Security Review
      → Change all default passwords
      → Enable two-factor authentication
      → Review database backups
      → Update CORS origins to your domain only

Deployment Command Example (Render.com):
  web: python -m uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 SUPPORT & RESOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Documentation Files in This Project:
  • README.md              → Start here for overview
  • QUICK_REFERENCE.md     → Cheat sheet and quick tips
  • SETUP.md               → Detailed setup instructions
  • CONFIGURATION.md       → Full configuration reference
  • PAYSTACK_SETUP.md      → M-Pesa integration details
  • This file (GUIDE.md)   → Complete project guide

External Resources:
  • Paystack Documentation:  https://paystack.com/docs
  • Paystack Support:        support@paystack.com
  • FastAPI Documentation:   https://fastapi.tiangolo.com
  • SQLAlchemy Documentation: https://docs.sqlalchemy.org
  • JavaScript MDN:          https://developer.mozilla.org

Getting Help:
  1. Read the documentation files listed above
  2. Check troubleshooting section in README.md
  3. View API docs at http://localhost:8000/docs
  4. Check backend terminal for error messages
  5. Check browser console (F12) for frontend errors
  6. Verify Paystack dashboard for payment status
  7. Contact Paystack support for payment issues

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ QUICK VERIFICATION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After starting the app, verify these work:

  □ http://localhost:8000/          → Shows home page
  □ http://localhost:8000/login.html → Shows login page
  □ http://localhost:8000/docs       → Shows API documentation
  □ http://localhost:8000/health     → Returns {"status": "healthy"}
  □ Can register new account         → Phone + password works
  □ Can login with credentials       → Returns JWT tokens
  □ Can apply for loan               → Loan appears in dashboard
  □ Fee calculation is correct       → Amount + fee = total
  □ Can view loan history            → Shows all your loans
  □ Can initiate payment             → Redirects to Paystack
  □ Dashboard updates after payment  → Loan marked as repaid

If all checks pass: ✅ You're ready to go live!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎉 YOU'RE ALL SET!

Start here:
  1. Read QUICK_REFERENCE.md for 30-second summary
  2. Get Paystack account and API keys
  3. Edit .env file with your keys
  4. Double-click RUN_APP.bat
  5. Test the application
  6. Deploy to production

Questions? Check the documentation files above or contact Paystack.

Happy lending! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Version: 1.0.0 | Last Updated: December 2024
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
