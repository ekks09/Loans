# 🚀 Push to GitHub - Quick Guide

## Option A: Use the Batch File (Easiest)

1. Open File Explorer
2. Navigate to: `C:\Users\USER\3D Objects\project\Loans`
3. Double-click: **`PUSH_TO_GITHUB.bat`**
4. Follow the prompts!

**What it does:**
- Sets up GitHub connection
- Pushes your code
- Opens GitHub in browser when done

---

## Option B: Manual PowerShell Commands

Open PowerShell and run these commands:

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/microloan.git

# Ensure branch is main
git branch -M main

# Push to GitHub
git push -u origin main
```

When prompted:
- **Username:** YOUR_USERNAME
- **Password:** Your Personal Access Token (see below)

---

## Getting Your Personal Access Token

### Step 1: Go to GitHub Settings
https://github.com/settings/tokens

### Step 2: Generate New Token
1. Click **"Generate new token"** → **"Generate new token (classic)"**
2. Fill in:
   - Name: `microloan-push`
   - Expiration: `90 days` (or your preference)
   - Scopes: Select **`repo`** (full control)
3. Click **"Generate token"**

### Step 3: Copy Token
- ⚠️ **IMPORTANT**: Copy it immediately! You won't see it again
- Don't share this token with anyone
- Keep it secure (treat like password)

---

## Expected Results

### While Pushing
```
Enumerating objects: 60, done.
Counting objects: 100%
Writing objects: 100%
...
* [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### After Success ✅
Your repository is now on GitHub!

Visit: `https://github.com/YOUR_USERNAME/microloan`

You should see:
- All 60+ files
- All commits
- All folders (backend/, frontend/, etc.)

---

## Verify It Worked

```powershell
# Check remote is configured
git remote -v

# Should show:
# origin  https://github.com/YOUR_USERNAME/microloan.git (fetch)
# origin  https://github.com/YOUR_USERNAME/microloan.git (push)

# Check commits were pushed
git log --oneline -5
```

---

## Troubleshooting

### Issue: "Repository already exists"
**Fix:**
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/microloan.git
git push -u origin main
```

### Issue: "Authentication failed"
**Fix:**
- Make sure you're using Personal Access Token, not password
- Token should be copied exactly (no extra spaces)
- Token should have `repo` scope selected

### Issue: "Permission denied (publickey)"
**Fix:**
- This is SSH key issue, use HTTPS instead:
```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/microloan.git
git push -u origin main
```

### Issue: "fatal: remote origin already exists"
**Fix:**
```powershell
git remote -v  # See what's configured
git remote remove origin  # Remove old one
git remote add origin https://github.com/YOUR_USERNAME/microloan.git
git push -u origin main
```

---

## What Gets Pushed

✅ **Included:**
- All Python code (backend/)
- Frontend (HTML, CSS, JavaScript)
- Configuration files
- Documentation guides
- Requirements.txt

❌ **Excluded (auto-ignored):**
- env/ folder (virtual environment)
- __pycache__/
- .env file (secrets)
- *.db (SQLite database)

---

## Next Step

After pushing to GitHub successfully, you're ready to deploy to Render!

See: `RENDER_FREE_TIER_SETUP.md`

---

## Summary

```
Your Code → GitHub → Render → Live App! 🚀
```

Good luck! 🎉
