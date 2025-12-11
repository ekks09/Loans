# Git Setup & Render Deployment Guide

## Essential Files Only (Pushing to Git)

### ✅ KEEP & PUSH TO GIT
```
microloan/
├── prod_app.py                 # Production FastAPI server
├── requirements.txt            # Python dependencies
├── .gitignore                  # Exclude unnecessary files
├── .env.example                # Template (no secrets!)
├── README.md                   # Project info
├── RENDER_DEPLOYMENT.md        # Setup guide
├── RENDER_DEPLOYMENT_CHECKLIST.md
├── infra/
│   └── render.yaml            # Render configuration
├── backend/
│   ├── requirements.txt        # Backend dependencies
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/            # User, Loan, Transaction models
│   │   ├── routers/           # Auth, loan, payments routes
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Paystack service
│   │   └── utils/             # Database, auth utilities
│   └── alembic/               # Migrations (optional)
└── frontend/
    ├── index.html
    ├── login.html
    ├── dashboard.html
    ├── loan_apply.html
    ├── payment.html
    ├── scripts/
    │   ├── api.js
    │   └── ui.js
    └── styles/
        ├── main.css
        ├── glass.css
        └── animations.css
```

### ❌ DO NOT PUSH (Add to .gitignore)
```
.env                           # Local secrets
env/                          # Virtual environment (~300MB)
__pycache__/                  # Python cache
.local/                       # Replit files
.replit                       # Replit config
*.db                          # SQLite databases
microloan.db                  # Development database
dev_app.py                    # Development server
dev_server.py                 # Old server
run.py, serve.py, etc.        # Old server files
*.bat                         # Windows batch files
.vscode/, .idea/              # IDE configs
```

## Step 1: Initialize Git Repository

Open PowerShell in your project folder:

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Initialize git
git init

# Add all files (respecting .gitignore)
git add .

# Verify what will be pushed
git status
```

Verify output shows:
- ✅ `prod_app.py`
- ✅ `requirements.txt`
- ✅ `backend/` folder
- ✅ `frontend/` folder
- ❌ NO `env/` folder
- ❌ NO `__pycache__/`
- ❌ NO `.env` file

## Step 2: Create First Commit

```powershell
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

git commit -m "Initial commit: MicroLoan application with Paystack integration"
```

## Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Enter Repository name: **`microloan`**
3. Make it **Public** (free tier requirement)
4. Do NOT initialize with README, .gitignore, or license (you have them)
5. Click **"Create repository"**

## Step 4: Push to GitHub

```powershell
# Add remote origin (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/microloan.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

You'll be prompted for GitHub credentials. Use your GitHub username and a **Personal Access Token** (not password):
- Create token: https://github.com/settings/tokens
- Select: `repo` scope
- Copy and paste as password

## Step 5: Setup Render Free Web Service

### 5.1 Create Render Account
1. Go to https://render.com
2. Click **"Sign up"**
3. Use GitHub account (easier connection)
4. Click **"Authorize render"`

### 5.2 Create Web Service
1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect account"** (GitHub)
4. Find your **`microloan`** repository
5. Click **"Connect"**

### 5.3 Configure Service

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `microloan-api` |
| **Environment** | `Python 3` |
| **Region** | `Ohio` (us-east) or closest to you |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python prod_app.py` |
| **Plan** | `Free` (see plans below) |

### 5.4 Add Environment Variables

Click **"Add Environment Variable"** for each:

| Key | Value | Where to Get |
|-----|-------|--------------|
| `DATABASE_URL` | `postgresql://postgres:password@db.xxx.supabase.co:5432/postgres` | Supabase → Settings → Database → Connection string |
| `SECRET_KEY` | Generate with: `python -c "import secrets; print(secrets.token_urlsafe(32))"` | Generate new |
| `PAYSTACK_SECRET_KEY` | `sk_live_xxxxx` | Paystack → Settings → API Keys |
| `PAYSTACK_PUBLIC_KEY` | `pk_live_xxxxx` | Paystack → Settings → API Keys |
| `RENDER` | `true` | Fixed value |

⚠️ **IMPORTANT**: Keep `.env` file locally on your computer NEVER commit it to GitHub!

### 5.5 Deploy

1. Click **"Create Web Service"**
2. Wait 2-5 minutes for build to complete
3. You'll see: **`https://microloan-api.onrender.com`** (your app URL!)

## Step 6: Verify Deployment

### Test in Browser
1. Open: `https://microloan-api.onrender.com/health`
   - Should show: `{"status": "healthy", ...}`

2. Open: `https://microloan-api.onrender.com/`
   - Should show the login page

3. Open: `https://microloan-api.onrender.com/api/docs`
   - Should show API documentation

### Test Signup
1. Go to `https://microloan-api.onrender.com/login.html`
2. Click **"Sign Up"** tab
3. Enter:
   - Phone: `0712345678`
   - ID No: `12345678`
   - Password: `Test@123`
4. Click **"Create Account"**
5. Check if it redirects to dashboard (user created successfully!)

## Render Free Tier Limits

| Resource | Free Tier Limit |
|----------|-----------------|
| Web Service | 1 free instance |
| CPU | 0.5 CPU |
| RAM | 512 MB |
| Bandwidth | 100 GB/month |
| Auto-sleep | Spins down after 15 min inactivity |
| Cold start | ~30 seconds when waking up |

⚠️ **Note:** Free tier services spin down after 15 minutes of inactivity. They wake up on first request but take 30 seconds.

## Making Changes & Redeploying

After you make code changes:

```powershell
# Stage changes
git add .

# Commit
git commit -m "Your change description"

# Push to GitHub
git push origin main
```

Render automatically detects the push and redeploys your app! (2-5 minutes)

## Troubleshooting

### Issue: "Service failed to start"
Check Render Logs:
1. Dashboard → Your Service → Logs
2. Look for error messages
3. Common issues:
   - Missing environment variables
   - Database connection error
   - Typo in `prod_app.py`

### Issue: "Could not find DATABASE_URL"
Solution:
1. Render Dashboard → Your Service → Environment
2. Verify `DATABASE_URL` is set
3. Click "Save" to restart service

### Issue: "Cannot reach deployed app"
Solution:
1. Wait for build to complete (check status)
2. Fresh browser tab (Ctrl+Shift+Delete cache)
3. Check service is running (green "Live" status)

### Issue: "Database connection timeout"
Solution:
1. Verify Supabase instance is running
2. Check DATABASE_URL format is correct
3. Verify firewall allows Render IPs
   - Supabase → Settings → Database → Connection Pooling → Add Render IP

## Next Steps (After Deployment)

1. ✅ Push to GitHub
2. ✅ Deploy to Render
3. ✅ Test signup/login
4. Next: Test Paystack payment flow
5. Next: Set up custom domain (optional, requires paid plan)

## Useful Links

- **Render Dashboard:** https://dashboard.render.com
- **Render Docs:** https://render.com/docs
- **Supabase Connection:** https://supabase.com/docs/guides/database/connecting-to-postgres
- **Git Commands:** https://git-scm.com/docs

---

**Summary:**
- Git handles code versioning (essential files only)
- Render reads from GitHub and deploys automatically
- Supabase stores all your data
- Free tier is perfect for testing!
