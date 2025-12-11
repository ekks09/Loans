# Push to GitHub - Step by Step

## Prerequisites
You need:
1. GitHub account (https://github.com)
2. GitHub Personal Access Token (for authentication)

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: **`microloan`**
3. Select **Public**
4. Do NOT initialize with README (you have files)
5. Click **"Create repository"**

You'll see instructions like:
```
...or push an existing repository from the command line

git remote add origin https://github.com/YOUR_USERNAME/microloan.git
git branch -M main
git push -u origin main
```

## Step 2: Execute These Commands

Open PowerShell in your project folder:

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/microloan.git

# Ensure branch is main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Authentication

When prompted:
- **Username:** Your GitHub username
- **Password:** Your Personal Access Token (NOT your GitHub password!)

### How to Create Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "microloan-push"
4. Select scope: **`repo`** (full control of private repositories)
5. Click "Generate token"
6. Copy the token immediately (you won't see it again!)
7. Paste as password when prompted

## Expected Output

Should look like:
```
Enumerating objects: 60, done.
Counting objects: 100%
Writing objects: 100%
Receiving objects: 100%
...
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## Verify Success

```powershell
# Check remote is set
git remote -v

# Should show:
# origin  https://github.com/YOUR_USERNAME/microloan.git (fetch)
# origin  https://github.com/YOUR_USERNAME/microloan.git (push)

# Check logs
git log --oneline -5
```

Then visit your GitHub page: https://github.com/YOUR_USERNAME/microloan

You should see all your files! ✅
