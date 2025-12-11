import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./microloan.db")

# Fix postgres:// to postgresql:// for newer SQLAlchemy versions
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Detect environment
IS_PRODUCTION = os.getenv("RENDER") == "true" or os.getenv("ENVIRONMENT") == "production"

# Create engine with appropriate settings
if "supabase" in DATABASE_URL or "postgresql" in DATABASE_URL:
    # Production: Use NullPool for Supabase (remote PostgreSQL)
    # This avoids connection pooling issues with Render's ephemeral filesystem
    if IS_PRODUCTION:
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
    # SQLite fallback for development
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

