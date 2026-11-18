from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Database Setup (Using postgresql+psycopg2 as an example)
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise RuntimeError("DATABASE_URL is not set — check your .env file")
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
