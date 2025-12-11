# MicroLoan API

A complete, production-ready microloan web application with FastAPI backend, Supabase database, and Paystack M-Pesa integration.

## 1. Project Overview

MicroLoan is a microloan platform that enables users to:
- Register and authenticate using phone numbers
- Apply for loans ranging from KES 3,000 to KES 60,000
- View transparent processing fees
- Repay loans via M-Pesa through Paystack
- Track loan history and repayment status

### Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (Supabase)
- **Payments**: Paystack with M-Pesa integration
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Hosting**: Render.com

## 2. Backend Setup

### Prerequisites
- Python 3.11+
- PostgreSQL database (Supabase recommended)
- Paystack account

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd microloan/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
cp ../.env.example .env
# Edit .env with your actual values
```

5. Run database migrations:
```bash
alembic upgrade head
```

6. Start the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 3. Frontend Setup

The frontend is a static HTML/CSS/JS application.

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Serve the files using any static file server:
```bash
# Using Python
python -m http.server 5000

# Or using Node.js
npx serve -l 5000
```

3. Open `http://localhost:5000` in your browser

### Frontend Pages
- `index.html` - Landing page with features overview
- `login.html` - Login and registration
- `dashboard.html` - User dashboard with loan history
- `loan_apply.html` - Loan application with live preview

## 4. Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `SECRET_KEY` | JWT signing secret (min 32 chars) | Yes |
| `PAYSTACK_SECRET_KEY` | Paystack secret key | Yes |

### Example `.env` file:
```
DATABASE_URL=postgresql://user:password@db.supabase.co:5432/postgres
SECRET_KEY=your-super-secret-key-at-least-32-characters-long
PAYSTACK_SECRET_KEY=sk_live_xxxxxxxxxxxxx
```

## 5. Database Setup + Alembic Commands

### Supabase Setup

1. Create a new project at [supabase.com](https://supabase.com)
2. Go to Settings > Database
3. Copy the connection string (URI format)
4. Replace `[YOUR-PASSWORD]` with your database password
5. Use this as your `DATABASE_URL`

### Alembic Commands

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply all migrations
alembic upgrade head

# Downgrade one migration
alembic downgrade -1

# Show current revision
alembic current

# Show migration history
alembic history
```

## 6. Paystack Setup

### Getting API Keys

1. Create an account at [paystack.com](https://paystack.com)
2. Go to Settings > API Keys & Webhooks
3. Copy your Secret Key (starts with `sk_`)
4. For testing, use Test Secret Key
5. For production, use Live Secret Key

### Configuring M-Pesa

1. In Paystack Dashboard, go to Settings > Channels
2. Enable Mobile Money (Kenya - M-Pesa)
3. Connect your M-Pesa Till or Paybill
4. Complete verification if required

### Webhook Configuration

1. Go to Settings > API Keys & Webhooks
2. Add your webhook URL: `https://your-domain.com/api/payments/webhook`
3. Select events: `charge.success`, `charge.failed`

## 7. Render Deployment Steps

### Prerequisites
- GitHub repository with your code
- Render.com account
- Supabase database ready

### Deployment Steps

1. **Push code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Create Render Web Service**
   - Go to [render.com](https://render.com)
   - Click "New" > "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Service**
   - Name: `microloan-api`
   - Region: Choose closest to your users
   - Branch: `main`
   - Root Directory: Leave empty
   - Runtime: Python 3
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && chmod +x render_start.sh && ./render_start.sh`

4. **Add Environment Variables**
   - `DATABASE_URL`: Your Supabase connection string
   - `SECRET_KEY`: Click "Generate" for a secure key
   - `PAYSTACK_SECRET_KEY`: Your Paystack secret key

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Your API will be available at `https://microloan-api.onrender.com`

### Using render.yaml

Alternatively, use the included `render.yaml`:
1. Go to Render Dashboard
2. Click "New" > "Blueprint"
3. Connect your repository
4. Render will detect `render.yaml` and configure automatically

## 8. API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login user |
| POST | `/api/auth/refresh` | Refresh access token |
| GET | `/api/auth/me` | Get current user |
| POST | `/api/auth/otp/request` | Request OTP (optional) |
| POST | `/api/auth/otp/verify` | Verify OTP (optional) |

### Loans

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/loans/preview` | Preview loan with fees |
| POST | `/api/loans/apply` | Apply for a loan |
| GET | `/api/loans/history` | Get user's loan history |
| GET | `/api/loans/{id}` | Get specific loan |

### Payments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/payments/initialize` | Initialize payment |
| GET | `/api/payments/verify/{ref}` | Verify payment |
| POST | `/api/payments/webhook` | Paystack webhook |
| GET | `/api/payments/transactions` | Get transactions |

### Processing Fees

| Principal (KES) | Fee (KES) |
|-----------------|-----------|
| 3,000 | 200 |
| 5,000 | 350 |
| 6,000 - 8,000 | 460 |
| 10,000 | 1,000 |
| 20,000 | 2,000 |
| 30,000 | 3,000 |
| 40,000 | 4,000 |
| 50,000 | 5,000 |
| 60,000 | 6,000 |

## 9. Common Errors + Fixes

### Database Connection Errors

**Error**: `connection refused` or `timeout`
- **Fix**: Check your `DATABASE_URL` is correct
- **Fix**: Ensure your IP is whitelisted in Supabase

**Error**: `relation "users" does not exist`
- **Fix**: Run migrations: `alembic upgrade head`

### Authentication Errors

**Error**: `Could not validate credentials`
- **Fix**: Check if token is expired
- **Fix**: Ensure `SECRET_KEY` matches in all environments

**Error**: `Phone number already registered`
- **Fix**: Use a different phone number or login

### Payment Errors

**Error**: `Payment initialization failed`
- **Fix**: Verify `PAYSTACK_SECRET_KEY` is correct
- **Fix**: Check Paystack dashboard for API status

**Error**: `Transaction not found`
- **Fix**: Ensure reference is correct
- **Fix**: Payment may not have been created

### Deployment Errors

**Error**: `ModuleNotFoundError`
- **Fix**: Check `requirements.txt` includes all dependencies
- **Fix**: Rebuild the deployment

**Error**: `Port already in use`
- **Fix**: Use `PORT` environment variable
- **Fix**: Render provides this automatically

### Frontend Errors

**Error**: `Failed to fetch` in browser
- **Fix**: Check CORS settings in backend
- **Fix**: Ensure API URL is correct in `api.js`

**Error**: Blank page after login
- **Fix**: Check browser console for errors
- **Fix**: Verify tokens are being stored

## Support

For issues or questions:
1. Check the API documentation at `/docs`
2. Review Paystack documentation
3. Check Supabase status page
4. Open an issue on GitHub
