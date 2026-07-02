import sqlite3

DB_NAME = "app.db"


# -----------------------------
# GET CASES (SAFE + STABLE)
# -----------------------------
def get_cases():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # We use SELECT * because your DB schema is currently messy/wide (15 columns)
    c.execute("SELECT * FROM cases")

    rows = c.fetchall()
    conn.close()

    return rows


# -----------------------------
# OPTIONAL: DEBUG HELP
# -----------------------------
def debug_cases_schema():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("PRAGMA table_info(cases)")
    columns = c.fetchall()

    conn.close()
    return columns


# -----------------------------
# OPTIONAL: GET SINGLE CASE
# -----------------------------
def get_case_by_id(case_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT * FROM cases WHERE id = ?", (case_id,))
    row = c.fetchone()

    conn.close()
    return row


# -----------------------------
# OPTIONAL: INSERT CASE (SAFE FOR CURRENT SCHEMA)
# -----------------------------
def insert_case(data):
    """
    WARNING: This assumes your current 15-column structure.
    If you don’t use this function yet, ignore it.
    """

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO cases VALUES (
            NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, data)

    conn.commit()
    conn.close()
