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
# PAGE CONFIG (ALWAYS HERE)
# =========================
st.set_page_config(page_title="AUSTRAC SaaS Platform", layout="wide")

# =========================
# STEP 5 GOES HERE (SAFE AREA)
# =========================
# session_state
# logo loading
# header UI
# etc

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

    # =========================
    # INVESTOR LANDING PAGE
    # =========================
    st.title("🏢 AUSTRAC Compliance Intelligence Platform")

    st.markdown("""
    ### AI-powered AML / CTF Risk Monitoring System

    This platform helps detect and manage suspicious property transactions
    using real-time compliance workflows and risk scoring.

    ---
    
    #### 🚀 Key Features
    - Real-time risk scoring engine  
    - Case management system (OPEN / REVIEWING / CLOSED)  
    - Audit trail for compliance reporting  
    - Dashboard analytics for monitoring trends  

    ---
    
    #### 🧠 System Status
    - ✔ Live risk engine  
    - ✔ SQLite secure database  
    - ✔ Audit logging enabled  
    - ✔ SaaS architecture (Level 4)  
    """)

    st.divider()

    # =========================
    # DEMO LOGIN BOX
    # =========================
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.subheader("Secure Login")

        st.info("Demo credentials: admin / admin")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if authenticate(username, password):
                st.session_state.auth = True
                st.session_state.user = username
                log_action(username, "LOGIN")
                st.rerun()

            else:
                st.error("Invalid login")

    st.stop()
   
st.success(f"Logged in as {st.session_state.user}")

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["Dashboard", "Risk Engine", "Cases", "Audit Log"]
)

# =========================
# DASHBOARD
# =========================
with tab1:

    st.subheader("📊 Compliance Overview Dashboard")

    cases = get_cases()

    total_cases = len(cases)
    high_risk = len([c for c in cases if c[3] > 70])
    open_cases = len([c for c in cases if c[7] == "OPEN"])
    total_amount = sum([c[2] for c in cases]) if cases else 0

    # =========================
    # KPI CARDS
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", total_cases)
    col2.metric("High Risk", high_risk)
    col3.metric("Open Cases", open_cases)
    col4.metric("Total Exposure ($)", f"${total_amount:,.0f}")

    st.divider()

    # =========================
    # VISUAL INSIGHTS
    # =========================
    if cases:

        import pandas as pd

        df = pd.DataFrame(
            cases,
            columns=[
                "ID",
                "Property",
                "Amount",
                "Risk Score",
                "Status",
                "Created",
                "User",
                "Case Status"
            ]
        )

        st.markdown("### 📈 Risk Analytics")

        colA, colB = st.columns(2)

        with colA:
            st.markdown("#### Risk Score Distribution")
            st.bar_chart(df[["Risk Score"]])

        with colB:
            st.markdown("#### Transaction Volume")
            st.line_chart(df[["Amount"]])

        st.markdown("### 🧾 Latest Activity")

        st.dataframe(df.head(10), use_container_width=True)

    else:
        st.info("No data available. Run a risk check to populate dashboard.")

# =========================
# RISK ENGINE
# =========================
with tab2:

    st.subheader("Risk Engine (Rule-Based)")

    property_id = st.text_input("Property ID")
    amount = st.number_input("Transaction Amount", min_value=0)

    if st.button("Run Risk Check"):

        risk_score = min(100, int(amount / 5000))
        status = "HIGH" if risk_score > 70 else "LOW"

        add_case(
            property_id,
            amount,
            risk_score,
            status,
            st.session_state.user
        )

        log_action(st.session_state.user, f"RISK_CHECK {property_id}")

        st.success("Case created successfully")
        st.metric("Risk Score", risk_score)
        st.write("Status:", status)

# =========================
# CASES
# =========================
with tab3:

    st.subheader("Case Management System")

    data = get_cases()

    if data:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Property",
                "Amount",
                "Risk Score",
                "Status",
                "Created",
                "User",
                "Case Status"
            ]
        )

        # =========================
        # FILTERS
        # =========================
        col1, col2 = st.columns(2)

        status_filter = col1.selectbox(
            "Filter Risk Level",
            ["ALL", "HIGH", "LOW"]
        )

        case_filter = col2.selectbox(
            "Filter Case Status",
            ["ALL", "OPEN", "REVIEWING", "CLOSED"]
        )

        # Apply filters safely
        if status_filter != "ALL":
            df = df[df["Status"] == status_filter]

        if case_filter != "ALL":
            df = df[df["Case Status"] == case_filter]

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No cases yet. Run a risk check first.")

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

# =========================
# FOOTER
# =========================
st.divider()

st.caption(
    "© 2026 AUSTRAC Compliance SaaS Platform | Version 1.0 | "
    "Demo Platform | Built with Streamlit"
)
