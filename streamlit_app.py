import streamlit as st
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Platform",
    page_icon="🏠",
    layout="wide"
)

# ---------------- LOGIN ----------------
USERS = {
    "admin": "admin123",
    "agent": "agent123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

def login():
    st.title("🔐 Login - AUSTRAC Compliance Platform")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

def logout():
    st.sidebar.write(f"Logged in as: {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

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
    st.title("🏠 AUSTRAC Compliance Dashboard")
    logout()

    st.write(f"Welcome, **{st.session_state.user}**")

    bulk_input = st.text_area("Enter transactions (one per line)")

    if st.button("Run Analysis"):

        if not bulk_input.strip():
            st.warning("Enter transactions")
        else:
            lines = bulk_input.strip().split("\n")

            results = []

            for i, line in enumerate(lines, start=1):
                score, level, flags = analyze(line)

                results.append({
                    "id": i,
                    "input": line,
                    "score": score,
                    "level": level,
                    "flags": flags
                })

            st.subheader("Results")

            for r in results:
                with st.expander(f"Transaction {r['id']} - {r['level']}"):
                    st.write(r)

            st.download_button(
                "Download Report",
                json.dumps(results, indent=2),
                file_name="austrac_report.json",
                mime="application/json"
            )
