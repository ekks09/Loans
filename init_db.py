import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from backend.app.utils.database import Base, engine
from backend.app.models.user import User
from backend.app.models.loan import Loan
from backend.app.models.transaction import Transaction

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
