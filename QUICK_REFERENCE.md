# MicroLoan - Quick Reference Card

## 🚀 30-Second Startup

1. Get Paystack account at https://paystack.com
2. Copy your API keys (Secret & Public)
3. Edit `.env` and paste the keys
4. Double-click `RUN_APP.bat`
5. Done! App opens at http://localhost:8000

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `RUN_APP.bat` | ⭐ Click this to start everything |
| `.env` | Your Paystack API keys go here |
| `README.md` | How to use the app |
| `PAYSTACK_SETUP.md` | How to set up Paystack |
| `SETUP.md` | Detailed installation guide |

---

## 🔧 Startup Scripts

```bash
RUN_APP.bat          # Full startup (everything)
START_BACKEND.bat    # Backend only
SETUP_DATABASE.bat   # Reset database
CLEANUP.bat          # Remove virtual environment
```

---

## 🌐 Access Points

| URL | Purpose |
|-----|---------|
| http://localhost:8000 | Frontend (home page) |
| http://localhost:8000/docs | API documentation (Swagger) |
| http://localhost:8000/dashboard.html | User dashboard |
| http://localhost:8000/payment.html | Payment page |

---

## 💻 Paystack Setup (5 minutes)

### Step 1: Create Account
- Go to https://paystack.com/signup
- Verify email and phone
- Complete KYC (ID, bank details)

### Step 2: Get Keys
- Go to Settings ⚙️
- Click API Keys & Webhooks
- Copy Secret Key and Public Key

### Step 3: Enable M-Pesa
- Settings → Payment Options
- Select Kenya
- Toggle M-Pesa ON

### Step 4: Paste Keys
- Open `.env` file
- Paste:
  ```
  PAYSTACK_SECRET_KEY=sk_test_xxxxx
  PAYSTACK_PUBLIC_KEY=pk_test_xxxxx
  ```

### Step 5: Test
- Run `RUN_APP.bat`
- Register account
- Apply for loan
- Click "Pay Now"
- Test payment completes

---

## 📱 Using the App

### Register
- Go to http://localhost:8000
- Click "Sign Up"
- Phone: `0712345678` (or any 10 digits)
- Password: `test123` (or any password)
- Click "Create Account"

### Apply for Loan
- Click "Apply for Loan"
- Select amount (3,000 - 60,000 KES)
- See fee calculation
- Click "Apply Now"
- Loan approved instantly!

### Make Payment
- Go to Dashboard
- Find your loan
- Click "Pay Now"
- Enter M-Pesa phone number
- Click "Proceed to Payment"
- Complete M-Pesa on your phone
- Done! Loan marked as repaid

---

## 🆘 Troubleshooting (Quick Fixes)

### Backend won't start
```bash
# Port 8000 in use
netstat -ano | findstr :8000
taskkill /PID <pid_number> /F

# Or use different port
python -m uvicorn backend.app.main:app --port 8001
```

### "Cannot connect to server"
```bash
# Make sure .env exists and has:
PAYSTACK_SECRET_KEY=sk_test_xxxxx
PAYSTACK_PUBLIC_KEY=pk_test_xxxxx
```

### "Database errors"
```bash
# Recreate database
python init_db.py
```

### "Payment fails"
- Check Paystack keys are correct
- Verify M-Pesa is enabled
- Try with test number first
- Check internet connection

### "Login/Signup fails"
- Check backend is running
- Check phone number format (0712345678)
- Try different password
- Clear browser cache (Ctrl+Shift+Delete)

---

## 🔐 Security Reminders

⚠️ **IMPORTANT**
- Keep `.env` secret (don't share)
- Don't commit `.env` to git
- Change `SECRET_KEY` before production
- Use HTTPS for live site
- Never expose API keys

---

## 🎯 Key Features

✅ User registration & authentication
✅ Loan application with auto-calculated fees
✅ Paystack M-Pesa integration
✅ Payment verification & webhooks
✅ Loan history & dashboard
✅ Responsive mobile design
✅ Error handling & validation
✅ Secure password hashing

---

## 📊 Fee Structure

| Amount | Fee |
|--------|-----|
| 3,000 | 200 |
| 5,000 | 350 |
| 6,000-8,000 | 460 |
| 10,000 | 1,000 |
| 20,000 | 2,000 |
| 30,000 | 3,000 |
| 40,000 | 4,000 |
| 50,000 | 5,000 |
| 60,000 | 6,000 |

---

## 📈 Loan Limits

- **Starting Limit:** 5,000 KES
- **Maximum Limit:** 60,000 KES
- **Increase:** +2,000 KES per repaid loan
- **Active Loans:** Only 1 at a time
- **Repayment:** Via M-Pesa payment

---

## 🔗 Useful Links

- **Paystack Dashboard:** https://dashboard.paystack.com
- **Paystack Docs:** https://paystack.com/docs
- **API Swagger Docs:** http://localhost:8000/docs
- **Your Database:** microloan.db (SQLite)

---

## 📋 Testing Checklist

- [ ] App starts without errors
- [ ] Can register new account
- [ ] Can login with credentials
- [ ] Can apply for loan
- [ ] Fee calculates correctly
- [ ] Can initiate payment
- [ ] Redirects to Paystack
- [ ] Payment flow works
- [ ] Loan marked as repaid
- [ ] Can see in transaction history

---

## 🚀 Production Checklist

- [ ] Get live Paystack keys
- [ ] Update `.env` with live keys
- [ ] Remove `_test_` from keys
- [ ] Change `SECRET_KEY` to strong random
- [ ] Switch to PostgreSQL database
- [ ] Enable HTTPS/SSL
- [ ] Update CORS origins
- [ ] Set up webhook URL
- [ ] Configure banking settlement
- [ ] Test with real payments
- [ ] Set up monitoring/logs

---

## 💬 Need Help?

1. **Setup Issues:** Check `README.md`
2. **Paystack Issues:** Check `PAYSTACK_SETUP.md`
3. **Detailed Guide:** Check `CONFIGURATION.md`
4. **API Errors:** Check http://localhost:8000/docs
5. **Paystack Support:** support@paystack.com

---

## 🎓 Learning Resources

- **FastAPI:** https://fastapi.tiangolo.com
- **Paystack:** https://paystack.com/docs
- **SQLAlchemy:** https://docs.sqlalchemy.org
- **JavaScript Fetch:** https://developer.mozilla.org/en-US/docs/Web/API/fetch

---

**You're all set!** 🎉

Questions? Check the documentation files or contact Paystack support.
