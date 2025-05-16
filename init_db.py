# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("AcadKoDataBase.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            hash TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized!")

if __name__ == "__main__":
    init_db()