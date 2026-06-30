import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join("database", "app.db")

def get_conn():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        action TEXT,
        timestamp TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        property_id TEXT,
        amount REAL,
        risk_score INTEGER,
        status TEXT,
        created_at TEXT,
        created_by TEXT
    )
    """)

    conn.commit()
    conn.close()

def log_action(user, action):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "INSERT INTO audit_log (user, action, timestamp) VALUES (?, ?, ?)",
        (user, action, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

def add_case(property_id, amount, risk_score, status, created_by):
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases (property_id, amount, risk_score, status, created_at, created_by)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (property_id, amount, risk_score, status, datetime.now().isoformat(), created_by))

    conn.commit()
    conn.close()

def get_cases():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM cases ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def get_logs():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM audit_log ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows
