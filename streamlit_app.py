import streamlit as st
import sqlite3
import json

st.set_page_config(
    page_title="AUSTRAC Admin Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

# default users
c.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123')")
c.execute("INSERT OR IGNORE INTO users VALUES ('agent1', 'agent123')")
c.execute("INSERT OR IGNORE INTO users VALUES ('agent2', 'agent123')")
conn.commit()

def authenticate(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def add_user(username, password):
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def get_users():
    c.execute("SELECT username FROM users")
    return c.fetchall()

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ---------------- LOGIN ----------------
def login():
    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")

# ---------------- RISK ENGINE ----------------
def analyze(text):
    text = text.lower()

    score = 0
    flags = []

    if "cash" in text:
        score += 30
        flags.append("Cash transaction")

    if "offshore" in text:
        score += 25
        flags.append("Offshore involvement")

    if "third party" in text:
        score += 20
        flags.append("Third-party payment")

    if "urgent" in text:
        score += 10
        flags.append("Urgency pressure")

    if "multiple deposits" in text:
        score += 25
        flags.append("Structured payments")

    if score >= 50:
        level = "🔴 HIGH RISK"
    elif score >= 20:
        level = "🟠 MEDIUM RISK"
    else:
        level = "🟢 LOW RISK"

    return score, level, flags

# ---------------- APP ----------------
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("Admin Panel")
    st.sidebar.write(f"Logged in as: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    st.title("🏠 AUSTRAC Admin Dashboard")

    # ---------------- USER MANAGEMENT ----------------
    st.subheader("User Management")

    col1, col2 = st.columns(2)

    with col1:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create User"):
            if add_user(new_user, new_pass):
                st.success("User created")
            else:
                st.error("User already exists")

    with col2:
        st.write("Existing Users")
        users = get_users()
        for u in users:
            st.write("•", u[0])

    # ---------------- ANALYSIS ----------------
    st.subheader("Compliance Checker")

    bulk_input = st.text_area("Enter transactions (one per line)")

    if st.button("Run Analysis"):

        lines = bulk_input.strip().split("\n")
        results = []

        for i, line in enumerate(lines, start=1):
            score, level, flags = analyze(line)

            results.append({
                "user": st.session_state.user,
                "id": i,
                "input": line,
                "score": score,
                "level": level,
                "flags": flags
            })

        st.subheader("Results")

        for r in results:
            with st.expander(f"{r['level']} - Transaction {r['id']}"):
                st.write(r)

        st.download_button(
            "Download Report",
            json.dumps(results, indent=2),
            file_name="austrac_admin_report.json",
            mime="application/json"
        )
