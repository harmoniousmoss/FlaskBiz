# seed.py

from models.user_model import User

# Create a seed user
seed_user = User.create_user(
    full_name="Test User",
    email="test@example.com",
    password="testpassword"
)

print("Seed user created:", seed_user)
