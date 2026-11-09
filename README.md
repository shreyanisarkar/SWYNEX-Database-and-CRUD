# SWYNEX Database and CRUD API

## Project Description

This project is developed as part of the SWYNEX Technologies Backend Developer Internship (Task 2).

The project implements a RESTful API using Python and Flask, integrated with an SQLite database to perform CRUD (Create, Read, Update, Delete) operations on student records.

The API allows users to add, retrieve, update, and delete student information.

## Technologies Used

- Python
- Flask
- SQLite
- Flask-SQLAlchemy
- Postman
- Git and GitHub

## Project Structure

```text
SWYNEX-Database-and-CRUD/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
└── students.db
```

## Database Details

Database Name: students.db

Table Name: students

The database stores the following information:

| Field | Description |
|---|---|
| id | Unique student ID |
| name | Student name |
| email | Student email address |
| course | Student course |

SQLite is used as the database because it is lightweight and is supported directly by Python.

## API Endpoints

Base URL: `http://127.0.0.1:5000`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/students` | Add a new student |
| GET | `/api/students` | Retrieve all students |
| GET | `/api/students/<id>` | Retrieve a student by ID |
| PUT | `/api/students/<id>` | Update student details |
| DELETE | `/api/students/<id>` | Delete a student |

## CRUD Operations

### 1. Create (POST)

Adds a new student record to the database.

Example JSON:

```json
{
    "name": "Shreyani Sarkar",
    "email": "shreyani@gmail.com",
    "course": "B.Tech CSE"
}
```

### 2. Read (GET)

Retrieves all student records stored in the SQLite database.

### 3. Update (PUT)

Updates the existing information of a student using their unique ID.

### 4. Delete (DELETE)

Deletes a student record from the database using their unique ID.

## Testing

The API was tested using Postman.

The following operations were successfully tested:

- POST – Student record created successfully (201 Created).
- GET – Student records retrieved successfully (200 OK).
- PUT – Student record updated successfully.
- DELETE – Student record deleted successfully (200 OK).

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/shreyanisarkar/SWYNEX-Database-and-CRUD.git
```

### Step 2: Open the Project Folder

```bash
cd SWYNEX-Database-and-CRUD
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application

```bash
python app.py
```

The application will run at:

`http://127.0.0.1:5000`

## API Health Check

Visit:

`http://127.0.0.1:5000/health`

Expected response:

```json
{
    "application": "SWYNEX API",
    "status": "healthy",
    "version": "1.0.0"
}
```

## Learning Outcomes

Through this project, I learned:

- How to develop RESTful APIs using Flask.
- How to connect Python applications with SQLite databases.
- How to perform CRUD operations.
- How to test API endpoints using Postman.
- How to manage and upload projects using Git and GitHub.

## Author

**Shreyani Sarkar**

Backend Developer Intern – SWYNEX Technologies

GitHub: https://github.com/shreyanisarkar