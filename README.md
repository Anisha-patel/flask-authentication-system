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

## Project Structure

```text
python-fullstack-task3/
│
├── app.py              # Main Flask application logic & routes
├── database.db          # SQLite database (auto-generated)
├── README.md            # Project documentation
│
├── templates/
│   ├── login.html       # Login page
│   ├── register.html    # User registration page
│   ├── dashboard.html   # Main authenticated dashboard
│   ├── students.html    # Student list view (Read)
│   ├── add_student.html # Add student form (Create)
│   └── edit_student.html# Edit student form (Update)
│
└── static/
    └── style.css        # Basic CSS styles

