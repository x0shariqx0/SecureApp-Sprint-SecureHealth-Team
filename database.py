import sqlite3
from werkzeug.security import generate_password_hash

from config import Config


def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            diagnosis TEXT NOT NULL,
            assigned_doctor_id INTEGER,
            FOREIGN KEY (assigned_doctor_id) REFERENCES users(id)
        )
        """
    )

    conn.commit()
    conn.close()


def seed_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS count FROM users")
    user_count = cursor.fetchone()["count"]

    if user_count == 0:
        admin_password = generate_password_hash("admin123")
        doctor_password = generate_password_hash("doctor123")

        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            ("Admin User", "admin@example.com", admin_password, "admin"),
        )
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            ("Doctor User", "doctor@example.com", doctor_password, "doctor"),
        )

        cursor.execute("SELECT id FROM users WHERE role = 'doctor' LIMIT 1")
        doctor = cursor.fetchone()
        doctor_id = doctor["id"] if doctor else None

        patients = [
            ("Alice Smith", 30, "Hypertension", doctor_id),
            ("Bob Johnson", 45, "Diabetes", doctor_id),
            ("Charlie Lee", 27, "Seasonal Allergy", doctor_id),
        ]

        cursor.executemany(
            """
            INSERT INTO patients (name, age, diagnosis, assigned_doctor_id)
            VALUES (?, ?, ?, ?)
            """,
            patients,
        )

    conn.commit()
    conn.close()
