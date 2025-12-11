# 🚀 Quick Render Deployment - 5 Minutes

## Step 1: Connect GitHub (2 minutes)

### 1.1 Create GitHub Repo
1. Go to https://github.com/new
2. Name: `microloan`
3. Select **Public** (free tier requirement)
4. Don't initialize README/gitignore
5. Click **"Create repository"**

### 1.2 Push Your Code
```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/microloan.git

# Push to GitHub
git branch -M main
git push -u origin main
```

When prompted for password, use a **Personal Access Token**:
- Go to: https://github.com/settings/tokens
- Click "Generate new token (classic)"
- Select `repo` scope
- Click "Generate token"
- Copy & paste as password

**Result:** Your code is now on GitHub! ✅

---

## Step 2: Deploy on Render (3 minutes)

### 2.1 Go to Render Dashboard
1. Open https://render.com
2. Click **"Sign up"** (use GitHub to sign up faster)
3. Authorize Render to access GitHub

### 2.2 Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Click **"Connect account"** (connect GitHub)
3. Find **`microloan`** repo
4. Click **"Connect"**

### 2.3 Configure Settings
Fill in exactly as shown:

| Field | Value |
|-------|-------|
| Name | `microloan-api` |
| Environment | `Python 3` |
| Region | `Ohio` (or closest to you) |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python prod_app.py` |
| Plan | `Free` |

**Don't change anything else!**

### 2.4 Add Environment Variables
Click **"Add Environment Variable"** and paste these **one by one**:

#### 1. DATABASE_URL
```
postgresql://postgres:password@db.xxx.supabase.co:5432/postgres
```
(Get from Supabase Settings → Database)

#### 2. SECRET_KEY
Generate a secure key (run this on your computer):
```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
Copy the output and paste it.

#### 3. PAYSTACK_SECRET_KEY
```
sk_live_xxxxx
```
(Get from Paystack Dashboard → Settings → API Keys)

#### 4. PAYSTACK_PUBLIC_KEY
```
pk_live_xxxxx
```
(Get from Paystack Dashboard → Settings → API Keys)

#### 5. RENDER
```
true
```

### 2.5 Click "Create Web Service"
- Wait 2-5 minutes for build
- You'll see: **`https://microloan-api.onrender.com`**

**Your app is LIVE!** 🎉

---

## Step 3: Test Your App (1 minute)

### 3.1 Test Health Check
Open in browser:
```
https://microloan-api.onrender.com/health
```

Should see:
```json
{"status": "healthy", "version": "1.0.0", "service": "MicroLoan API"}
```

### 3.2 Test Frontend
Open:
```
https://microloan-api.onrender.com/
```

Should see login page ✅

### 3.3 Test API Docs
Open:
```
https://microloan-api.onrender.com/api/docs
```

Should see Swagger API documentation ✅

### 3.4 Test Signup
1. Go to: `https://microloan-api.onrender.com/login.html`
2. Click **"Sign Up"** tab
3. Enter:
   - Phone: `0712345678`
   - ID No: `12345678`
   - Password: `Test@123`
4. Click **"Create Account"**
5. Should redirect to dashboard ✅

---

## 🎉 YOU'RE DONE!

Your app is deployed on Render with Supabase database!

| Component | Status |
|-----------|--------|
| Frontend | ✅ https://microloan-api.onrender.com |
| API | ✅ https://microloan-api.onrender.com/api |
| Database | ✅ Supabase PostgreSQL |
| SSL/HTTPS | ✅ Free with Render |

---

## Making Changes

After modifying your code:

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Stage changes
git add .

# Commit
git commit -m "Your changes description"

# Push to GitHub
git push origin main
```

**Render automatically detects the push and redeploys!** (2-5 min)

---

## Troubleshooting

### Issue: Build fails
1. Check Render Logs (your service → Logs)
2. Common: Missing environment variable
3. Fix: Add missing variable in Environment tab

### Issue: "Could not connect to database"
1. Verify DATABASE_URL in Render Environment
2. Verify Supabase instance is running
3. Try restarting service (click "Restart")

### Issue: Static files missing (404)
1. Ensure frontend/ folder is pushed to Git
2. Check `prod_app.py` can find frontend folder
3. Restart service

### Issue: App too slow/crashes
1. Free tier has 512MB RAM
2. Upgrade to paid plan for better performance
3. Or optimize code

---

## Next Steps

1. ✅ **App Deployed** - https://microloan-api.onrender.com
2. **Test Paystack** - Try applying for a loan
3. **Monitor** - Check Render logs regularly
4. **Custom Domain** - (Optional, requires paid plan)

**Documentation:** See `RENDER_DEPLOYMENT.md` for detailed info

Good luck! 🚀
