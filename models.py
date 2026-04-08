from database import get_db_connection


class User:
    @staticmethod
    def create(name, email, password, role):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (name, email, password, role),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def all_doctors():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE role = 'doctor'")
        doctors = cursor.fetchall()
        conn.close()
        return doctors


class Patient:
    @staticmethod
    def all_records():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT p.*, u.name AS doctor_name
            FROM patients p
            LEFT JOIN users u ON p.assigned_doctor_id = u.id
            ORDER BY p.id DESC
            """
        )
        patients = cursor.fetchall()
        conn.close()
        return patients

    @staticmethod
    def find_by_id(patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT p.*, u.name AS doctor_name
            FROM patients p
            LEFT JOIN users u ON p.assigned_doctor_id = u.id
            WHERE p.id = ?
            """,
            (patient_id,),
        )
        patient = cursor.fetchone()
        conn.close()
        return patient

    @staticmethod
    def create(name, age, diagnosis, assigned_doctor_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO patients (name, age, diagnosis, assigned_doctor_id)
            VALUES (?, ?, ?, ?)
            """,
            (name, age, diagnosis, assigned_doctor_id),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(patient_id, name, age, diagnosis, assigned_doctor_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE patients
            SET name = ?, age = ?, diagnosis = ?, assigned_doctor_id = ?
            WHERE id = ?
            """,
            (name, age, diagnosis, assigned_doctor_id, patient_id),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
        conn.commit()
        conn.close()
