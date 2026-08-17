from flask import Flask, render_template, request, redirect, session, jsonify, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from functools import wraps
app = Flask(__name__)
import os
app.secret_key = os.environ.get("SECRET_KEY", "fallback-dev-key")

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper
 
 
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        if session.get('role') != 'admin':
            flash("Admins only. You don't have access to that page.")
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        db = get_db()
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)",(username, password))
        db.commit()
        db.close()
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            session['role'] = (
          user['role']
          if ('role' in user.keys() and user['role'])
          else 'user'
      )
            return redirect('/dashboard')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        db = get_db()
        db.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )
        db.commit()
        db.close()
        return redirect('/students')

    return render_template('add_student.html')


@app.route('/students')
def students():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    data = db.execute("SELECT * FROM students").fetchall()
    return render_template('student.html', students=data)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    student = db.execute(
        "SELECT * FROM students WHERE id = ?", (id,)).fetchone()
    if request.method == 'POST':
        db.execute(
            "UPDATE students SET name=?, email=?, course=? WHERE id=?",
            (
                request.form['name'],
                request.form['email'],
                request.form['course'],
                id
            )
        )
        db.commit()
        return redirect('/students')
    return render_template('edit_student.html', student=student)


@app.route('/delete/<int:id>')
def delete_student(id):
    if 'user' not in session:
        return redirect('/login')

    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect('/students')

@app.route('/admin')
@admin_required
def admin_dashboard():
    db = get_db()
    users = db.execute("SELECT id, username, role FROM users").fetchall()
    students_list = db.execute("SELECT * FROM students").fetchall()
    db.close()
    return render_template('admin_dashboard.html', users=users, students=students_list)
 
 
@app.route('/admin/delete/<int:id>')
@admin_required
def admin_delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    return redirect('/students')

@app.route('/api/students', methods=['GET'])
@login_required
def api_get_students():
    db = get_db()
    students = db.execute("SELECT * FROM students").fetchall()
    return jsonify([dict(row) for row in students])
 
 
@app.route('/api/students/<int:id>', methods=['GET'])
@login_required
def api_get_student(id):
    db = get_db()
    row = db.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    db.close()
    if row is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(dict(row))
 
 
@app.route('/api/students', methods=['POST'])
@login_required
def api_add_student():
    data = request.get_json()
    db = get_db()
    db.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (data['name'], data['email'], data['course'])
    )
    db.commit()
    return jsonify({"message": "Student added successfully"})
 
 
@app.route('/api/students/<int:id>', methods=['PUT'])
@login_required
def api_update_student(id):
    data = request.get_json()
    db = get_db()
    db.execute(
        "UPDATE students SET name=?, email=?, course=? WHERE id=?",
        (data['name'], data['email'], data['course'], id)
    )
    db.commit()
    return jsonify({"message": "Student updated"})
 
 
@app.route('/api/students/<int:id>', methods=['DELETE'])
@admin_required
def api_delete_student(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,))
    db.commit()
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(debug=False)