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
