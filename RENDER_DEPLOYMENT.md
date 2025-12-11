# MicroLoan - Render Deployment Guide

Deploy your MicroLoan application to Render with Supabase PostgreSQL database.

## Prerequisites

- GitHub account (for pushing your code)
- Render account (https://render.com)
- Supabase account (https://supabase.com)
- Paystack account for M-Pesa integration

## Step 1: Set Up Supabase Database

### 1.1 Create Supabase Project
1. Go to https://supabase.com and sign in
2. Click "New Project"
3. Fill in the project name: `microloan`
4. Choose region (recommended: closest to your users)
5. Click "Create new project"

### 1.2 Get Database Credentials
1. Go to **Settings** → **Database**
2. Copy the **Connection String** (URI)
3. The format is: `postgresql://postgres:password@host:5432/postgres`
4. Save this securely - you'll need it for Render

### 1.3 Create Tables (Initial Migration)
1. In Supabase, go to **SQL Editor**
2. Create a new query and run:

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(20) UNIQUE NOT NULL,
    id_number VARCHAR(20) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    loan_limit INTEGER DEFAULT 5000,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Loans table
CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    amount INTEGER NOT NULL,
    duration INTEGER DEFAULT 30,
    interest_rate FLOAT DEFAULT 0.03,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    loan_id INTEGER NOT NULL REFERENCES loans(id) ON DELETE CASCADE,
    amount INTEGER NOT NULL,
    type VARCHAR(20),
    reference VARCHAR(255),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_id_number ON users(id_number);
CREATE INDEX idx_loans_user_id ON loans(user_id);
CREATE INDEX idx_transactions_loan_id ON transactions(loan_id);
```

## Step 2: Push Code to GitHub

### 2.1 Initialize Git Repository
```powershell
cd "C:\Users\USER\3D Objects\project\Loans"
git init
git add .
git commit -m "Initial commit: MicroLoan application"
```

### 2.2 Create GitHub Repository
1. Go to https://github.com/new
2. Create repository name: `microloan`
3. Don't initialize with README (you have one)
4. Click "Create repository"

### 2.3 Push to GitHub
```powershell
git remote add origin https://github.com/YOUR_USERNAME/microloan.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Render

### 3.1 Create Render Web Service
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account
4. Select your `microloan` repository
5. Configure:
   - **Name**: `microloan-api`
   - **Region**: Select closest to users (e.g., us-east-1)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python prod_app.py`

### 3.2 Set Environment Variables
In the Render dashboard, add these environment variables:

1. **DATABASE_URL** (Required)
   - Paste your Supabase connection string
   - Format: `postgresql://postgres:password@db.xxx.supabase.co:5432/postgres`

2. **SECRET_KEY** (Required)
   - Generate a secure key:
     ```powershell
     python -c "import secrets; print(secrets.token_urlsafe(32))"
     ```
   - Or let Render generate one automatically

3. **PAYSTACK_SECRET_KEY**
   - From https://dashboard.paystack.com → Settings → API Keys
   - Copy **Secret Key**

4. **PAYSTACK_PUBLIC_KEY**
   - From https://dashboard.paystack.com → Settings → API Keys
   - Copy **Public Key**

5. **RENDER** 
   - Set value to: `true`

### 3.3 Deploy
1. Click **"Create Web Service"**
2. Render will automatically build and deploy
3. Wait for deployment to complete (2-5 minutes)
4. You'll get a URL like: `https://microloan-api.onrender.com`

## Step 4: Verify Deployment

### 4.1 Test API
1. Open: `https://your-app.onrender.com/health`
2. Should see:
   ```json
   {
     "status": "healthy",
     "version": "1.0.0",
     "service": "MicroLoan API"
   }
   ```

3. API Docs: `https://your-app.onrender.com/api/docs`
4. Frontend: `https://your-app.onrender.com/`

### 4.2 Test Signup
1. Go to `https://your-app.onrender.com/login.html`
2. Click "Sign Up"
3. Fill in:
   - Phone: 0712345678
   - ID No: 12345678
   - Password: Test@123
4. Click "Create Account"
5. Should redirect to dashboard

## Step 5: Update Frontend URLs (If Needed)

Edit `frontend/scripts/api.js` to update API_BASE_URL:

```javascript
const API_BASE_URL = window.location.origin; // This auto-detects the domain
```

Then push changes:
```powershell
git add .
git commit -m "Update API URL for production"
git push origin main
```

Render will automatically rebuild and deploy.

## Troubleshooting

### Issue: "Could not connect to database"
**Solution:**
- Verify DATABASE_URL is correct in Render environment variables
- Ensure Supabase instance is running
- Check password doesn't have special characters (or URL-encode them)

### Issue: "Application crashes on startup"
**Solution:**
- Check Render logs: Go to your service → Logs
- Ensure all required environment variables are set
- Verify `requirements.txt` has all dependencies

### Issue: "Database tables not found"
**Solution:**
- Run SQL migration in Supabase SQL Editor (see Step 1.3)
- Or manually create tables using Supabase dashboard

### Issue: "Static files not found"
**Solution:**
- Ensure `frontend/` folder is pushed to GitHub
- Check file permissions in Render logs

## Monitoring & Maintenance

### View Logs
1. Render Dashboard → Your Web Service → Logs
2. Useful commands:
   ```
   # Check health
   curl https://your-app.onrender.com/health
   
   # View recent errors
   # In Render logs, filter by "ERROR"
   ```

### Update Environment Variables
1. Render Dashboard → Your Service → Environment
2. Edit variables
3. Click "Save"
4. Render automatically restarts the service

### Deploy New Changes
```powershell
git add .
git commit -m "Your changes"
git push origin main
```
Render will automatically build and deploy!

## Production Best Practices

✅ **DO:**
- Use strong SECRET_KEY
- Keep Paystack keys secure (never commit to repo)
- Monitor logs regularly
- Set up regular Supabase backups
- Use HTTPS (Render provides free SSL)

❌ **DON'T:**
- Commit `.env` files to GitHub
- Use test/demo Paystack keys in production
- Share environment variables publicly
- Use default database credentials

## Getting Help

- **Render Docs**: https://render.com/docs
- **Supabase Docs**: https://supabase.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Paystack Docs**: https://paystack.com/docs

## Next Steps

1. ✅ Database deployed (Supabase)
2. ✅ Backend deployed (Render)
3. ✅ Frontend served from backend
4. Next: Set up Paystack M-Pesa integration
5. Next: Configure custom domain (optional)

---

**Deployment Summary:**
- **Frontend**: Served from `https://your-app.onrender.com`
- **API**: Available at `https://your-app.onrender.com/api`
- **Database**: Supabase PostgreSQL (remote)
- **Status**: Live and ready for users!
