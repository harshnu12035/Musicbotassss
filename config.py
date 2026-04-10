import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")

SESSION = os.getenv("SESSION", "your_session_string")

# volume 1.0 = normal, 2.0 = boosted
BOOST_LEVEL = float(os.getenv("BOOST_LEVEL", "1.5"))