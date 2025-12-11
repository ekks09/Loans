# Render + Supabase Deployment Checklist

## Quick Start (5 Steps)

### 1. Supabase Setup (5 minutes)
- [ ] Create Supabase project at https://supabase.com
- [ ] Copy database connection string
- [ ] Run SQL migration in SQL Editor (see RENDER_DEPLOYMENT.md)

### 2. GitHub Setup (5 minutes)
- [ ] Create GitHub repository
- [ ] Push code: `git push origin main`

### 3. Render Setup (5 minutes)
- [ ] Create new Web Service on Render
- [ ] Connect GitHub repository
- [ ] Set Build Command: `pip install -r requirements.txt`
- [ ] Set Start Command: `python prod_app.py`

### 4. Environment Variables (2 minutes)
Add to Render:
```
DATABASE_URL = postgresql://postgres:password@db.xxx.supabase.co:5432/postgres
SECRET_KEY = [generate secure key]
PAYSTACK_SECRET_KEY = sk_live_xxxxx
PAYSTACK_PUBLIC_KEY = pk_live_xxxxx
RENDER = true
```

### 5. Deploy & Test (2 minutes)
- [ ] Click "Create Web Service" on Render
- [ ] Wait for deployment
- [ ] Test: https://your-app.onrender.com/health
- [ ] Test Frontend: https://your-app.onrender.com/

## Files Modified for Production

| File | Purpose |
|------|---------|
| `prod_app.py` | Production FastAPI server for Render |
| `backend/app/utils/database.py` | Production connection pooling |
| `requirements.txt` | Root-level dependencies for Render |
| `infra/render.yaml` | Render configuration |
| `.env.example` | Template for Supabase credentials |

## Key URLs After Deployment

```
Frontend:    https://your-app.onrender.com
API Docs:    https://your-app.onrender.com/api/docs
Health:      https://your-app.onrender.com/health
Login:       https://your-app.onrender.com/login.html
Dashboard:   https://your-app.onrender.com/dashboard.html
```

## Environment Variables Reference

| Variable | Example | Where to Get |
|----------|---------|--------------|
| `DATABASE_URL` | `postgresql://postgres:pwd@db.xxx.supabase.co:5432/postgres` | Supabase → Settings → Database |
| `SECRET_KEY` | `random-secure-string` | Generate with `python -c "import secrets; print(secrets.token_urlsafe(32))"` |
| `PAYSTACK_SECRET_KEY` | `sk_live_xxxxx` | Paystack Dashboard → API Keys |
| `PAYSTACK_PUBLIC_KEY` | `pk_live_xxxxx` | Paystack Dashboard → API Keys |
| `RENDER` | `true` | Set in Render |

## Testing Endpoints

```bash
# Health Check
curl https://your-app.onrender.com/health

# API Info
curl https://your-app.onrender.com/api

# Login (POST)
curl -X POST https://your-app.onrender.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"0712345678","password":"test123"}'

# Register (POST)
curl -X POST https://your-app.onrender.com/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"phone":"0712345678","id_number":"12345678","password":"test123"}'
```

## Monitoring

**Check Logs:**
1. Render Dashboard → Your Service → Logs
2. Filter for errors
3. Look for database connection issues

**Restart Service:**
1. Render Dashboard → Your Service
2. Click "Restart" button
3. Service redeploys with latest code

**Update Variables:**
1. Render Dashboard → Your Service → Environment
2. Edit any variable
3. Click "Save"
4. Service automatically restarts

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| "Could not connect to database" | Check DATABASE_URL in Render env vars |
| "Tables not found" | Run SQL migration in Supabase SQL Editor |
| "Import error: cannot find module" | Ensure module is in requirements.txt |
| "Static files 404" | Verify frontend/ folder pushed to GitHub |
| "CORS errors" | Already enabled in prod_app.py |

## Post-Deployment Steps

1. **Test Signup/Login**
   - Go to https://your-app.onrender.com/login.html
   - Create test account
   - Verify database saves user

2. **Test Paystack Integration**
   - Apply for loan
   - Test payment initialization
   - Verify Paystack webhook works

3. **Set Custom Domain** (Optional)
   - Render Dashboard → Your Service → Settings
   - Add custom domain
   - Update DNS records with your registrar

4. **Set Up Monitoring** (Optional)
   - Enable alerts in Render
   - Monitor database usage in Supabase
   - Set up error tracking

## Database Management

**Backup:**
1. Supabase Dashboard → Database → Backups
2. Create manual backup before major updates

**Monitor:**
1. Supabase Dashboard → Logs
2. Check for connection errors
3. Monitor query performance

**Scaling:**
1. Supabase offers free tier with 500MB storage
2. Upgrade plan if needed
3. Monitor usage in Project Settings

## Support & Documentation

- **Render Docs:** https://render.com/docs
- **Supabase Docs:** https://supabase.com/docs  
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Paystack Docs:** https://paystack.com/docs

---

**Next Level:** After successful deployment, consider:
- Setting up CI/CD pipeline
- Automated database backups
- Performance monitoring
- Custom domain
- SSL certificate (auto with Render)
