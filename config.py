import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-secret-key")
    DATABASE = os.getenv("DATABASE_PATH", "patient_records.db")
    SEED_DB = os.getenv("SEED_DB", "true")
