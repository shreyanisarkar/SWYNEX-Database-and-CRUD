from flask import Flask, request, jsonify
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "development-key")

# Database location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "students.db")


# Connect to database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database table automatically
def create_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "SWYNEX Database and CRUD API",
        "message": "Welcome to SWYNEX Student Management API",
        "status": "running"
    })


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "application": "SWYNEX CRUD API",
        "status": "healthy",
        "version": "1.0.0"
    })


# CREATE - Add a student
@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    if not all(isinstance(x, str) and x.strip()
               for x in [name, email, course]):
        return jsonify({
            "error": "Name, email and course are required"
        }), 400

    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name.strip(), email.strip(), course.strip())
        )

        conn.commit()

        student_id = cursor.lastrowid

        return jsonify({
            "message": "Student created successfully",
            "student": {
                "id": student_id,
                "name": name.strip(),
                "email": email.strip(),
                "course": course.strip()
            }
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

    finally:
        conn.close()


# READ - Get all students
@app.route("/api/students", methods=["GET"])
def get_students():

    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students ORDER BY id"
    ).fetchall()

    conn.close()

    return jsonify({
        "students": [dict(student) for student in students]
    })


# READ - Get one student
@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"student": dict(student)})


# UPDATE - Update student details
@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if student is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    name = data.get("name", student["name"])
    email = data.get("email", student["email"])
    course = data.get("course", student["course"])

    if not all(isinstance(x, str) and x.strip()
               for x in [name, email, course]):
        conn.close()
        return jsonify({
            "error": "Name, email and course cannot be empty"
        }), 400

    try:
        conn.execute(
            """UPDATE students
               SET name = ?, email = ?, course = ?
               WHERE id = ?""",
            (name.strip(), email.strip(), course.strip(), student_id)
        )

        conn.commit()

        return jsonify({
            "message": "Student updated successfully",
            "student": {
                "id": student_id,
                "name": name.strip(),
                "email": email.strip(),
                "course": course.strip()
            }
        })

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

    finally:
        conn.close()


# DELETE - Delete a student
@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    conn = get_db_connection()

    cursor = conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    deleted = cursor.rowcount

    conn.close()

    if deleted == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student deleted successfully"
    })


# Start application
if __name__ == "__main__":
    create_table()
    app.run(debug=True)