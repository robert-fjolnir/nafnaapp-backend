from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv



load_dotenv("../.env")

DATABASE_URL = os.getenv("DATABASE_URL")

print(DATABASE_URL)

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()