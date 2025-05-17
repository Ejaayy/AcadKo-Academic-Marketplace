import sqlite3  # Add this import
import helpers
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_login import login_required

app = Flask(__name__)
app.secret_key = "my_super_secret_key_123456"

def get_db_connection():
    conn = sqlite3.connect("AcadKoDataBase.db")
    conn.row_factory = sqlite3.Row  # lets you access columns by name
    return conn

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")  # Fixed: Removed `db.`
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            return render_template("register.html", error="All fields are required")

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if username/email already exists
        existing_user = cursor.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?", 
            (username, email)
        ).fetchone()

        if existing_user:
            conn.close()
            return render_template("register.html", error="Username or email already exists")

        # Hash password and insert new user
        hash_pw = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO users (username, email, hash) VALUES (?, ?, ?)",
            (username, email, hash_pw)
        )
        conn.commit()
        conn.close()

        return render_template("login.html") 

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    user_id = session.get("user_id")
    #if not user_id:
     #   return redirect(url_for("login"))

    conn = get_db_connection()   # Get DB connection
    cursor = conn.cursor()       # Get cursor

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    conn.close()                 # Close connection

    return render_template("dashboard.html", user=row)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/contact")
def contact():
    return render_template("contact.html")                      

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html")

        # Open database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query database for email (or username if you prefer)
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()

        conn.close()

        # Ensure email exists and password is correct
        if not row or not check_password_hash(row["hash"], password):
            return render_template("login.html")

        # Login success, store session
        session["user_id"] = row["id"]
        print("✅ User login valid")

        return redirect(url_for("dashboard"))
    
    else:
        return render_template("login.html")

@app.route('/private_profile', methods=['GET', 'POST'])
def private_profile():
    # Get the user_id from the session (logged-in user)
    user_id = session.get('user_id')
    if not user_id:
        # If no user_id found, redirect to login page
        return redirect(url_for('login'))

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Handle form submission for editing profile fields
        field = request.form.get('field')  # which field user wants to update
        value = request.form.get('value')  # new value entered by the user

        # Only allow updating these specific fields for safety
        allowed_fields = {'email', 'linkedin', 'description', 'experience', 'certifications', 'skills'}

        if field in allowed_fields:
            # Update the corresponding field in the database for this user
            cursor.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (value, user_id))
            conn.commit()

        conn.close()

        # Redirect back to profile page, with edit mode still ON (edit='true' in URL)
        return redirect(url_for('private_profile', edit='true'))

    # If GET request, fetch the user info to display
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    # Check if the URL query parameter 'edit' is 'true', so we know
    # whether to show editable forms or just view mode.
    edit = request.args.get('edit') == 'true'

    # Render the profile page with user data and edit flag
    return render_template("private_profile_layout.html", user=user, edit=edit)


if __name__ == "__main__":
    app.run(debug=True)