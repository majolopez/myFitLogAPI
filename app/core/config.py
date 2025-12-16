import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(f"Loaded SUPABASE_URL: {SUPABASE_URL}")
print(f"Loaded SUPABASE_KEY: {SUPABASE_KEY}")   