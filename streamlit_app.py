import streamlit as st
import os
from PIL import Image
import pandas as pd

from utils.auth import authenticate
from utils.db import init_db, log_action, add_case, get_cases, get_logs

# =========================
# INIT DB
# =========================
init_db()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC SaaS Platform",
    layout="wide"
)

# =========================
# LOAD LOGO
# =========================
logo = Image.open(os.path.join("assets", "logo.png"))

# =========================
# SESSION STATE
# =========================
if "auth" not in st.session_state:
    st.session_state.auth = False

if "user" not in st.session_state:
    st.session_state.user = ""

# =========================
# HEADER
# =========================
col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo, width=90)

with col2:
    st.title("AUSTRAC Compliance SaaS Platform")
    st.caption("AML / CTF Risk Intelligence Engine")

st.divider()

# =========================
# LOGIN
# =========================
if not st.session_state.auth:

    st.subheader("Secure Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.auth = True
            st.session_state.user = username
            log_action(username, "LOGIN")
            st.rerun()
        else:
            st.error("Invalid login (use admin / admin)")

    st.stop()

st.success(f"Logged in as {st.session_state.user}")

# =========================
# TABS (NO SIDEBAR)
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["Dashboard", "Risk Engine", "Cases", "Audit Log"]
)

# =========================
# DASHBOARD
# =========================
with tab1:

    st.subheader("System Overview")

    cases = get_cases()
    logs = get_logs()

    colA, colB, colC = st.columns(3)

    colA.metric("Total Cases", len(cases))
    colB.metric("Audit Events", len(logs))
    colC.metric("System Status", "ACTIVE")

    st.info("Real-time AML / CTF monitoring system running (free SQLite version).")

# =========================
# RISK ENGINE
# =========================
with tab2:

    st.subheader("Risk Engine (Rule-Based)")

    property_id = st.text_input("Property ID")
    amount = st.number_input("Transaction Amount", min_value=0)

    if st.button("Run Risk Check"):

        # SIMPLE FREE SCORING MODEL
        risk_score = min(100, int(amount / 5000))

        status = "HIGH" if risk_score > 70 else "LOW"

        add_case(property_id, amount, risk_score, status)
        log_action(st.session_state.user, f"RISK_CHECK {property_id}")

        st.success("Case created successfully")

        st.metric("Risk Score", risk_score)
        st.write("Status:", status)

# =========================
# CASES
# =========================
with tab3:

    st.subheader("Case Management")

    data = get_cases()

    if data:
        df = pd.DataFrame(
            data,
            columns=["ID", "Property", "Amount", "Risk Score", "Status", "Created"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No cases yet.")

# =========================
# AUDIT LOG
# =========================
with tab4:

    st.subheader("Audit Trail")

    logs = get_logs()

    if logs:
        df = pd.DataFrame(
            logs,
            columns=["ID", "User", "Action", "Timestamp"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No audit logs yet.")
