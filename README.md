This repo tracks progress across Task 2 → Task 5 in one evolving Flask app.
See tags for each stage: `task2`, `task3`, `task4` ,`task5`

# Python Full Stack Web Development — Task 2
### User Authentication System (Register, Login, Logout) using Flask

## Project Flow

This project builds on Task 1 by adding a login system — users can register, log in, and see a dashboard only logged-in users can access.

**Registering:** The user enters a username and password. The app scrambles the password (called **hashing**) before saving it, so the real password is never stored.

**Logging in:** The user enters their details again. The app scrambles the typed password the same way and checks if it matches the saved version. If it matches, login succeeds.

**Staying logged in:** After login, the app creates a small note called a **session**, attached to the browser. This is how it remembers you're logged in as you move between pages.

**Protected dashboard:** The app checks for that session note before showing the dashboard. No note means no access — the user gets sent back to login instead.

**Logging out:** The session note is deleted, so the app forgets you were logged in.

**In short:** signup saves a scrambled password, login checks it and gives a session pass, the dashboard only opens with that pass, and logout takes it away.

---

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Security:** Werkzeug (password hashing)
- **Sessions:** Flask's built-in session system

---

## Features
- Register with a hashed password
- Login with username and password
- Session-based login tracking
- Protected dashboard (logged-in users only)
- Secure logout

---

## How to Run
```bash
pip install flask werkzeug
python app.py
```
Open: `http://127.0.0.1:5000/register`

---

## What I Learned
This task helped me understand how login systems work — password hashing, sessions, and restricting access to protected pages.

# Flask Student Management System (Task 3)

A secure, database-driven Web Application built with Flask and SQLite. This project extends the Task-2 authentication system by implementing full CRUD (Create, Read, Update, Delete) capabilities for managing student records,only accessable by authenticated users.

## Features

- **User Authentication (Task 2)**: Secure user registration and login with password hashing using Werkzeug and session-based route protection.
- **Protected Dashboard**: Central hub accessible only after logging in.
- **CRUD Operations (Task 3)**:
  - **Create**: Add new student details (Name, Email, Course).
  - **Read**: Display all stored student records in a dynamic HTML table.
  - **Update**: Edit existing student details.
  - **Delete**: Remove a student record from the database.
- **Database Persistence**: Automatic setup and storage using SQLite (`database.db`).
- **Security**: Direct URL access to dashboard and CRUD routes without logging in redirects to `/login`.

---

# Flask Student Management System (Task 4)
 
This is Task 3 (student CRUD app) upgraded with:
- User roles (admin / user)
- An admin-only panel
- REST APIs that return JSON

## Key Features

## Key Features

* **User Login & Security**: Users can register and log in safely. Passwords are saved securely using Werkzeug hashing.
* **Role-Based Permissions**: Admin users get special access. Custom checks (`@admin_required`, `@login_required`) stop regular users from deleting students or managing accounts.
* **Student Management Interface**: Simple web pages to view, add, edit, and delete student records easily.
* **REST APIs**: Built-in API endpoints that return data in clean JSON format for testing or linking with other apps.

---

## API Reference

| Endpoint | Method | Authorization | Description |
| :--- | :--- | :--- | :--- |
| `/api/students` | `GET` | Login Required | Retrieves all student records |
| `/api/students/<id>` | `GET` | Login Required | Retrieves details for a specific student by ID |
| `/api/students` | `POST` | Login Required | Adds a new student record (JSON body required) |
| `/api/students/<id>` | `PUT` | Login Required | Updates an existing student record (JSON body required) |
| `/api/students/<id>` | `DELETE` | Admin Only | Deletes a student record by ID |

---

## Example API Requests & Responses

### 1. Get Single Student (`GET /api/students/2`)

**Response Status:** 
```json
{
  "id": 2,
  "name": "Anisha",
  "email": "anisha123@gmail.com",
  "course": "CSE"
}
```
# Flask Student Management System (Task 5)

This task takes the app built in Task 4 and puts it live on the web. Instead of running only on a personal computer, it's now hosted online so anyone with the link can use it.

---

## What Changed?

Before this step, the project only ran on a local machine (`127.0.0.1:5000`). Task 5 was all about making it safe, stable, and accessible to the public.

* **Safety First:** Debug mode was turned off, and the secret key (used for secure login sessions) was removed from the code and saved as a hidden environment variable.
* **Production Web Server:** Flask’s built-in starter server was replaced with **Gunicorn**, a proper web server made to handle real web traffic. 
* **Procfile:** A file named `Procfile` tells the hosting platform how to start the app:
```
web: gunicorn app:app
```
**requirements.txt:** Lists every package the app depends on (Flask, Werkzeug, gunicorn, etc.), so the cloud server knows exactly what to install before running the app.
**Deployment:** The project is deployed on **Render**, connected directly to this GitHub repo. Every push to `main` triggers Render to rebuild and redeploy automatically.

## Live URL
🔗 https://flask-authentication-system-s7ms.onrender.com
 
---
 
## Technologies Used (Additional for Task 5)
- **WSGI Server:** Gunicorn
- **Hosting:** Render (free tier)
- **Environment Config:** Python's `os.environ`
---

## Environment Variables
 
| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Used by Flask to sign session cookies securely |
 
Set in Render under Environment → Environment Variables, never committed to GitHub.
 
---
 
## Deployment Steps
1. Disabled debug mode (`app.run(debug=False)`)
2. Moved `app.secret_key` to read from an environment variable
3. Created `requirements.txt` listing all dependencies
4. Created `Procfile` with `web: gunicorn app:app`
5. Pushed everything to GitHub
6. Created a Web Service on Render, connected to this repo
7. Set Build Command: `pip install -r requirements.txt`
8. Set Start Command: `gunicorn app:app`
9. Added `SECRET_KEY` as an environment variable on Render
10. Deployed and tested the live URL — login, dashboard, admin panel, and APIs all verified working
---

## Project Structure
 
```text
flask-authentication-system/
│
├── app.py                 # Main Flask application logic (Auth, RBAC, CRUD, & REST APIs)
├── database.db            # SQLite database (stores users & students data)
├── requirements.txt       # Python dependencies for deployment
├── Procfile                # Tells the hosting platform how to run the app (gunicorn)
├── README.md               # Complete multi-task project documentation
│
├── templates/
│   ├── login.html          # Login page
│   ├── register.html       # User registration page
│   ├── dashboard.html      # Standard user dashboard
│   ├── admin_dashboard.html # Admin-only dashboard (RBAC)
│   ├── students.html       # Student list view (Read)
│   ├── add_student.html    # Add student form (Create)
│   └── edit_student.html   # Edit student form (Update)
│
└── static/
    └── style.css            # Styling for UI components
```