import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Detect environment
IS_PRODUCTION = os.getenv("RENDER") == "true" or os.getenv("ENVIRONMENT") == "production"

# For Render production, DATABASE_URL MUST be set and must be PostgreSQL
if IS_PRODUCTION:
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is required for Render production deployment")
    if not ("postgresql" in DATABASE_URL or "postgres" in DATABASE_URL):
        raise ValueError("DATABASE_URL must be a PostgreSQL connection string for production (Supabase)")

# Fix postgres:// to postgresql:// for newer SQLAlchemy versions
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Default to SQLite for local development if DATABASE_URL not set
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./microloan.db"

# Create engine with appropriate settings
if DATABASE_URL and ("supabase" in DATABASE_URL or "postgresql" in DATABASE_URL):
    # PostgreSQL/Supabase configuration
    if IS_PRODUCTION:
        # Production: Use NullPool for Render with Supabase
        # NullPool avoids connection pooling issues with Render's ephemeral filesystem
        engine = create_engine(
            DATABASE_URL,
            poolclass=NullPool,
            connect_args={
                "connect_timeout": 10,
                "application_name": "microloan_app"
            },
            echo=False
        )
    else:
        # Development: Use QueuePool with connection pooling
        engine = create_engine(
            DATABASE_URL,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_recycle=3600,
            connect_args={"connect_timeout": 10},
            echo=False
        )
else:
    # SQLite for local development only
    if IS_PRODUCTION:
        raise ValueError("SQLite cannot be used in production. Set DATABASE_URL to Supabase PostgreSQL connection string.")
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Database session dependency for FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

