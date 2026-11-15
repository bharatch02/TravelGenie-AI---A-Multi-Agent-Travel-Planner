import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(
        database_url,
        connect_timeout=30
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print("Database connected successfully!")
            print(cur.fetchone())

except Exception as e:
    print("Database connection failed:", e)