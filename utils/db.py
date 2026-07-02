import sqlite3
from datetime import datetime

DB_NAME = "database/app.db"

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
            buyer_name TEXT,
            buyer_type TEXT,
            source_of_funds TEXT,
            cash_payment INTEGER,
            overseas_funds INTEGER,
            pep INTEGER,
            sanctions INTEGER,
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

    # REPORTS TABLE
    c.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id INTEGER,
            property TEXT,
            report_text TEXT,
            created TEXT
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
def add_case(
    property_id,
    amount,
    buyer_name,
    buyer_type,
    source_of_funds,
    cash_payment,
    overseas_funds,
    pep,
    sanctions,
    risk_score,
    status,
    user
):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases (
            property,
            amount,
            buyer_name,
            buyer_type,
            source_of_funds,
            cash_payment,
            overseas_funds,
            pep,
            sanctions,
            risk_score,
            status,
            created,
            user,
            case_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        property_id,
        amount,
        buyer_name,
        buyer_type,
        source_of_funds,
        int(cash_payment),
        int(overseas_funds),
        int(pep),
        int(sanctions),
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
    
# =========================
# GET REPORTS
# =========================
def get_reports(case_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        SELECT *
        FROM reports
        WHERE case_id = ?
        ORDER BY created DESC
    """, (case_id,))

    rows = c.fetchall()

    conn.close()

    return rows    
# =========================
# SAVE REPORT
# =========================
def save_report(case_id, property_id, report_text):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO reports (
            case_id,
            property,
            report_text,
            created
        )
        VALUES (?, ?, ?, ?)
    """, (
        case_id,
        property_id,
        report_text,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()    
