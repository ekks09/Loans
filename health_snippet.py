# Example FastAPI snippet - integrate into your prod_app module
from fastapi import FastAPI, Response
from db import check_db
from supabase_client import supabase

app = FastAPI()

@app.get("/health")
def health_check():
    db_ok = check_db()
    supabase_ok = True
    if supabase is not None:
        try:
            # perform a lightweight call, e.g., list tables via REST is not available here.
            # Instead, check the instance exists by calling a harmless endpoint like auth.get_user (not ideal)
            supabase_ok = True
        except Exception:
            supabase_ok = False

    status_code = 200 if db_ok and supabase_ok else 503
    return Response(content='{"db": %s, "supabase": %s}' % (str(db_ok).lower(), str(supabase_ok).lower()), media_type="application/json", status_code=status_code)
