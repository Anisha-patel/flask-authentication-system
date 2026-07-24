# Python Full Stack Web Development — Task 2
### User Authentication System (Register, Login, Logout) using Flask

## Project Flow

This project extends the Task 1 User Management app by adding authentication — users can register, log in, and access a protected dashboard.

**Registering:** The user enters a username and password. Before saving anything, the app scrambles the password using **hashing** — like shredding it so it can never be read back. Only this scrambled version gets stored in the database, never the real password.

**Logging in:** The user enters their credentials again. The app finds their username, scrambles the password they just typed the same way, and checks if it matches the stored version. If it matches, login succeeds.

**Staying logged in:** Once login succeeds, the app creates a small **session** — a note saying "this browser belongs to a logged-in user." This note is attached to the browser, so the server keeps recognizing the user as they move between pages.

**Protected dashboard:** Before loading the dashboard, the app checks if that session note exists. If yes, the dashboard loads. If no, the user is redirected back to login — so no one can access it just by typing the URL.

**Logging out:** The session note is deleted, so the app "forgets" the user was logged in, sending them back to login if they try to revisit the dashboard.

---

## Technologies Used
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Security:** Werkzeug (password hashing)
- **Sessions:** Flask's built-in session system

---

## Features
- User registration with hashed passwords
- Login with credential verification
- Session-based authentication
- Protected dashboard (logged-in users only)
- Secure logout

---

## How to Run
```bash
pip install flask werkzeug
python app.py
```
Then open: `http://127.0.0.1:5000/register`

---

## Learning Outcome
This task helped me understand how real apps secure user data — password hashing, session-based login, and protecting routes from unauthorized access.
