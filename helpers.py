import requests
from flask import redirect, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Generate a secure hash for the given password.
    """
    return generate_password_hash(password)

def verify_password(stored_hash, password_attempt):
    """
    Check if the provided password matches the stored hash.
    Returns True if it matches, False otherwise.
    """
    return check_password_hash(stored_hash, password_attempt)