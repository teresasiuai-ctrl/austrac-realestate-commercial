import streamlit as st
import sqlite3
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Platform",
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
c.execute("INSERT OR IGNORE INTO users VALUES ('agent', 'agent123')")
conn.commit()

def authenticate(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ---------------- LOGIN ----------------
def login():
    st.title("🔐 AUSTRAC Login Portal")

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

# ---------------- MAIN APP ----------------
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("User Panel")
    st.sidebar.write(f"Logged in as: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    st.title("🏠 AUSTRAC Compliance Dashboard (Multi-User)")

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
            with st.expander(f"{r['user']} - Transaction {r['id']} - {r['level']}"):
                st.write(r)

        st.download_button(
            "Download Report",
            json.dumps(results, indent=2),
            file_name="austrac_multi_user_report.json",
            mime="application/json"
        )
