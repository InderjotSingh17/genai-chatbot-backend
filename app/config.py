import os 
from dotenv import load_dotenv
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")
SYSTEM_PROMPT=os.getenv(
    "SYSTEM_PROMPT",
    "You are a technical tutor. Always start your answer with 'BRO:' and then explain the concept simply."
)
TEMPERATURE=float(os.getenv("TEMPERATURE",0.7))
MAX_TOKENS=int(os.getenv("MAX_TOKENS",300))
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")