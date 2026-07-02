import sqlite3

DB_NAME = "app.db"


# =============================
# CONNECTION
# =============================
def connect():
    return sqlite3.connect(DB_NAME)


# =============================
# CASES
# =============================
def get_cases():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM cases")
    rows = c.fetchall()

    conn.close()
    return rows


def add_case(case_data):
    """
    EXPECTS 12 values (excluding ID)
    """

    conn = connect()
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases VALUES (
            NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, case_data)

    conn.commit()
    conn.close()


# =============================
# STATUS UPDATE
# =============================
def update_case_status(case_id, status):
    conn = connect()
    c = conn.cursor()

    c.execute("""
        UPDATE cases
        SET status = ?
        WHERE id = ?
    """, (status, case_id))

    conn.commit()
    conn.close()


# =============================
# AUDIT LOG (simple)
# =============================
def log_action(user, action):
    print(f"[AUDIT] {user}: {action}")


# =============================
# COMPLIANCE REPORTS
# =============================
def init_reports_table():
    conn = connect()
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
    conn = connect()
    c = conn.cursor()

    c.execute("""
        INSERT INTO compliance_reports (case_id, report_text, created_by)
        VALUES (?, ?, ?)
    """, (case_id, report_text, created_by))

    conn.commit()
    conn.close()


def get_reports_by_case(case_id):
    conn = connect()
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
# =============================
# USERS TABLE (MULTI-USER SAAS)
# =============================

def init_users_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def create_user(username, password, role="officer"):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, password, role))

        conn.commit()

    except sqlite3.IntegrityError:
        pass  # user already exists

    conn.close()


def authenticate_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        SELECT id, username, role
        FROM users
        WHERE username = ? AND password = ?
    """, (username, password))

    user = c.fetchone()
    conn.close()

    return user
