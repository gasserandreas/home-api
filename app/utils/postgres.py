import os
from psycopg2.extras import RealDictCursor
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

def get_db_config():
    """Get database configuration from environment variables"""
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PORT = os.getenv("POSTGRES_PORT")

    if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT]):
        raise ValueError("Missing required database environment variables")
    
    return {
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT
    }

def get_db_connection():
    """Create and return a database connection"""
    db_config = get_db_config()
    return psycopg2.connect(
        **db_config,
        cursor_factory=RealDictCursor
    ) 