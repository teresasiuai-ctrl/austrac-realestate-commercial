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
