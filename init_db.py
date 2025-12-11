import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.utils.database import Base, engine
from backend.app.models.user import User
from backend.app.models.loan import Loan
from backend.app.models.transaction import Transaction

try:
    print("Testing database connection...")
    # Test the connection first
    with engine.connect() as connection:
        print("✓ Database connection successful!")
    
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created successfully!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nDatabase Configuration:")
    db_url = os.getenv("DATABASE_URL", "Not set")
    # Mask password for security
    if "password" in str(db_url).lower():
        display_url = db_url.split("@")[1] if "@" in db_url else "***"
        print(f"  Connecting to: ...@{display_url}")
    print(f"  Full URL: {db_url}")
    print("\nPlease verify:")
    print("  1. DATABASE_URL is correctly set in .env")
    print("  2. Supabase instance is running and accessible")
    print("  3. Network connection is available")
    sys.exit(1)
