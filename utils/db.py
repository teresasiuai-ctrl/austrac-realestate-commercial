import sqlite3
from datetime import datetime

DB_NAME = "app.db"

# =========================
# INIT DATABASE
# =========================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # CASES TABLE
    c.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property TEXT,
            amount REAL,
            risk_score INTEGER,
            status TEXT,
            created TEXT,
            user TEXT,
            case_status TEXT
        )
    """)

    # AUDIT LOG TABLE (FIXED)
    c.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# =========================
# LOG ACTION (FIXED)
# =========================
def log_action(user, action):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO audit_log (user, action, timestamp)
        VALUES (?, ?, ?)
    """, (user, action, datetime.now().isoformat()))

    conn.commit()
    conn.close()


# =========================
# ADD CASE
# =========================
def add_case(property_id, amount, risk_score, status, user):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases (
            property, amount, risk_score,
            status, created, user, case_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        property_id,
        amount,
        risk_score,
        status,
        datetime.now().isoformat(),
        user,
        "OPEN"
    ))

    conn.commit()
    conn.close()


# =========================
# GET CASES
# =========================
def get_cases():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM cases")
    rows = c.fetchall()

    conn.close()
    return rows


# =========================
# GET LOGS
# =========================
def get_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM audit_log")
    rows = c.fetchall()

    conn.close()
    return rows
