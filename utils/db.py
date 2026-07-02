import sqlite3

DB_NAME = "app.db"


# -----------------------------
# GET CASES
# -----------------------------
def get_cases():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM cases")
    rows = c.fetchall()

    conn.close()
    return rows


# -----------------------------
# ADD CASE (SAFE INSERT)
# -----------------------------
def add_case(case_data):
    """
    Expects full 15-column format (your current DB structure)
    """

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases VALUES (
            NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, case_data)

    conn.commit()
    conn.close()


# -----------------------------
# LOG ACTION (SIMPLE VERSION)
# -----------------------------
def log_action(action, user="system"):
    """
    Lightweight logger (no separate table required yet)
    """

    print(f"[AUDIT LOG] {user}: {action}")

# -----------------------------
# COMPLIANCE REPORTS (NEW)
# -----------------------------

def init_reports_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS compliance_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id INTEGER,
            report_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_by TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_report(case_id, report_text, created_by="admin"):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO compliance_reports (case_id, report_text, created_by)
        VALUES (?, ?, ?)
    """, (case_id, report_text, created_by))

    conn.commit()
    conn.close()


def get_reports_by_case(case_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        SELECT id, report_text, created_at
        FROM compliance_reports
        WHERE case_id = ?
        ORDER BY created_at DESC
    """, (case_id,))

    rows = c.fetchall()
    conn.close()
    return rows
    
