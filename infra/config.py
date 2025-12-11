import os

# Supabase / Postgres
DATABASE_URL = os.environ.get("DATABASE_URL")  # typical server-side Postgres URL
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

# Paystack
PAYSTACK_SECRET_KEY = os.environ.get("PAYSTACK_SECRET_KEY")
PAYSTACK_PUBLIC_KEY = os.environ.get("PAYSTACK_PUBLIC_KEY")
PAYSTACK_WEBHOOK_SECRET = os.environ.get("PAYSTACK_WEBHOOK_SECRET")

# App
SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret"
PORT = int(os.environ.get("PORT", "10000"))
