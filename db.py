import time
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from config import DATABASE_URL

logger = logging.getLogger("db")

engine = None

def init_db_engine(max_retries=5, backoff=2):
    global engine
    if not DATABASE_URL:
        logger.warning("No DATABASE_URL set; skipping DB engine initialization.")
        return None

    for attempt in range(1, max_retries + 1):
        try:
            engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
            # quick smoke test
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database connection established.")
            return engine
        except OperationalError as e:
            logger.warning("DB connection failed (attempt %d/%d): %s", attempt, max_retries, e)
            time.sleep(backoff * attempt)
    raise RuntimeError("Could not establish database connection after retries.")

def check_db() -> bool:
    try:
        if engine is None:
            init_db_engine()
        with engine.connect() as conn:
            r = conn.execute(text("SELECT 1")).scalar()
            return r == 1
    except Exception as e:
        logger.exception("DB check failed: %s", e)
        return False
