# Files to Remove Before Git Push

## SAFE TO DELETE (Won't affect production)

Run these commands in PowerShell to remove redundant files:

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# Remove old development server files
Remove-Item -Path dev_app.py -Force
Remove-Item -Path dev_server.py -Force  
Remove-Item -Path run.py -Force
Remove-Item -Path serve.py -Force
Remove-Item -Path start_server.py -Force
Remove-Item -Path main.py -Force

# Remove Windows batch files (not needed for web)
Remove-Item -Path RUN_APP.bat -Force
Remove-Item -Path START_BACKEND.bat -Force
Remove-Item -Path SETUP_DATABASE.bat -Force
Remove-Item -Path CLEANUP.bat -Force

# Remove development files
Remove-Item -Path .replit -Force
Remove-Item -Path pyproject.toml -Force
Remove-Item -Path postman_collection.json -Force

# Remove development SQLite database
Remove-Item -Path microloan.db -Force -ErrorAction SilentlyContinue

# These will be auto-ignored by .gitignore:
# - env/ (entire folder - huge!)
# - __pycache__/ 
# - .local/
# - .env (secrets file)
```

## FILES TO KEEP

```
✅ prod_app.py           → Production server
✅ requirements.txt      → Dependencies
✅ .gitignore           → Ignore unnecessary files
✅ .env.example         → Template (no secrets)
✅ README.md            → Project info
✅ RENDER_DEPLOYMENT.md → Deployment guide
✅ RENDER_DEPLOYMENT_CHECKLIST.md
✅ GIT_AND_RENDER_SETUP.md (this file)
✅ infra/render.yaml    → Render config
✅ backend/             → All models, routers, schemas
✅ frontend/            → All HTML, CSS, JS
```

## After Deletion, Run This

```powershell
cd "C:\Users\USER\3D Objects\project\Loans"

# See what will be committed
git status

# Should show:
# - Changes to be committed: (should be empty if you deleted before git add)
# - Your essential files
# - NO env/ folder
# - NO __pycache__/
# - NO .env file
```
