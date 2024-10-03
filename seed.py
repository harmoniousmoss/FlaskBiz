# seed.py

from models.user_model import User

# Attempt to create a seed user
seed_user = User.create_user(
    full_name="Test User",
    email="test@example.com",  # Duplicate emails will be blocked
    password="testpassword"
)

# Check if there was an error
if "error" in seed_user:
    print("Error creating user:", seed_user["error"])
else:
    print("Seed user created:", seed_user)
