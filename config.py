import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_PATH = os.path.join(
    BASE_DIR,
    "data",
    "pdf",
    "dsa_book.pdf"
)

DB_CONFIG = {
    "dbname": "rag_db",
    "user": "postgres",
    "password": "system",
    "host": "localhost",
    "port": 5432
}

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-api-key-here")
