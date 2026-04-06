import os
from dotenv import load_dotenv

load_dotenv()

SESSION = os.getenv("SESSION", "YOUR_SESSION_STRING_HERE")
BOOST_LEVEL = int(os.getenv("BOOST_LEVEL", "180"))  # 150-200 dB
API_ID = int(os.getenv("API_ID", "YOUR_API_ID"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH")
