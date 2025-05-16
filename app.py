import sqlite3  # Add this import
import helpers
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

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
    return render_template("dashboard.html")

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


if __name__ == "__main__":
    app.run(debug=True)