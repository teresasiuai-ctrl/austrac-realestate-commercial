import streamlit as st
import sqlite3
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

st.set_page_config(
    page_title="AUSTRAC AI Compliance Platform",
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

c.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123')")
c.execute("INSERT OR IGNORE INTO users VALUES ('agent1', 'agent123')")
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
    st.title("🔐 AUSTRAC Compliance Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid credentials")

# ---------------- AI ENGINE ----------------
def analyze(text):
    text = text.lower()

    score = 0
    flags = []
    explanation = []

    if "cash" in text:
        score += 30
        flags.append("Cash transaction")
        explanation.append("Cash reduces traceability and increases AML risk.")

    if "offshore" in text:
        score += 25
        flags.append("Offshore involvement")
        explanation.append("Offshore entities obscure ownership structures.")

    if "third party" in text:
        score += 20
        flags.append("Third-party payment")
        explanation.append("Third-party payments may hide source of funds.")

    if "urgent" in text:
        score += 10
        flags.append("Urgency pressure")
        explanation.append("Urgency may indicate attempt to bypass checks.")

    if "multiple deposits" in text:
        score += 25
        flags.append("Structured payments")
        explanation.append("Splitting payments may indicate structuring.")

    if score >= 50:
        level = "HIGH RISK"
    elif score >= 20:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return score, level, flags, explanation

# ---------------- PDF GENERATOR ----------------
def create_pdf(report_data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AUSTRAC Compliance Report")
    y -= 40

    c.setFont("Helvetica", 10)

    for r in report_data:
        c.drawString(50, y, f"Transaction {r['id']}")
        y -= 15

        c.drawString(60, y, f"Input: {r['input'][:80]}")
        y -= 15

        c.drawString(60, y, f"Score: {r['score']} | Level: {r['level']}")
        y -= 15

        c.drawString(60, y, f"Flags: {', '.join(r['flags'])}")
        y -= 25

        if y < 100:
            c.showPage()
            y = 750

    c.save()
    buffer.seek(0)
    return buffer

# ---------------- APP ----------------
if not st.session_state.logged_in:
    login()
else:
    st.sidebar.title("Admin Panel")
    st.sidebar.write(f"User: {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    st.title("🏠 AUSTRAC AI Compliance Dashboard")

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
        for u in get_users():
            st.write("•", u[0])

    st.subheader("AI Analysis + PDF Export")

    bulk_input = st.text_area("Enter transactions (one per line)")

    if st.button("Run Analysis"):

        lines = bulk_input.strip().split("\n")
        results = []

        for i, line in enumerate(lines, start=1):
            score, level, flags, explanation = analyze(line)

            results.append({
                "id": i,
                "input": line,
                "score": score,
                "level": level,
                "flags": flags,
                "explanation": explanation
            })

        st.subheader("Results")

        for r in results:
            st.write(r)

        pdf_file = create_pdf(results)

        st.download_button(
            "Download PDF Report",
            data=pdf_file,
            file_name="austrac_compliance_report.pdf",
            mime="application/pdf"
        )
