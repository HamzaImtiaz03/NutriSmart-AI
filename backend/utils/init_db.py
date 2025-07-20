from database.db import Base, engine
from database.models import MealLog

print("🔧 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
