import streamlit as st
import os
from PIL import Image
import pandas as pd

from utils.auth import authenticate
from utils.db import (
    init_db,
    log_action,
    add_case,
    get_cases,
    get_logs,
    save_report,
    get_reports,
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC SaaS Platform",
    layout="wide"
)
from pages.dashboard import show_dashboard
from pages.risk_engine import show_risk_engine
from pages.case_management import show_case_management

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Risk Engine", "Case Management"]
)

if page == "Dashboard":
    show_dashboard()

elif page == "Risk Engine":
    show_risk_engine()

elif page == "Case Management":
    show_case_management()
    
# =========================
# INIT DATABASE
# =========================
init_db()

# =========================
# STEP 5 GOES HERE (SAFE AREA)
# =========================
# session_state
# logo loading
# header UI
# etc

# =========================
# LOAD LOGO
# =========================
logo_path = os.path.join("assets", "logo.png")

logo = None
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    
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
    if logo:
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

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    if logo:
        st.image(logo, width=120)

    st.markdown("## AUSTRAC SaaS")

    st.success(f"Logged in as **{st.session_state.user}**")

    st.divider()

    st.write("### Platform Status")
    st.write("🟢 System Online")
    st.write("🟢 Database Connected")
    st.write("🟢 Audit Logging Active")

    st.divider()

    if st.button("Logout", use_container_width=True):
        st.session_state.auth = False
        st.session_state.user = ""
        st.rerun()

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

    st.title("Executive Compliance Dashboard")

    st.caption(
        "Real-time AML / CTF monitoring for property transactions"
    )

    st.divider()

    cases = get_cases()

    total_cases = len(cases)
    high_risk = len([c for c in cases if c[3] > 70])
    open_cases = len([c for c in cases if c[7] == "OPEN"])
    total_amount = sum([c[2] for c in cases]) if cases else 0

# =========================
# =========================
# KPI CARDS
# =========================
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "📁 Total Cases",
    total_cases
)

kpi2.metric(
    "🔴 High Risk Cases",
    high_risk
)

kpi3.metric(
    "🟡 Open Cases",
    open_cases
)

kpi4.metric(
    "💰 Total Exposure",
    f"${total_amount:,.0f}"
)

st.divider()

# =========================
# VISUAL INSIGHTS
# =========================
if cases:

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

        chart_df = (
            df.groupby("Status")["Amount"]
              .sum()
              .reset_index()
              .set_index("Status")
        )

        st.bar_chart(chart_df)

    st.markdown("### Recent Compliance Cases")

    st.dataframe(
        df.sort_values(by="Risk Score", ascending=False),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    case_id = st.number_input(
        "Case ID",
        min_value=1,
        step=1
    )

else:
    st.info("No data available. Run a risk check to populate dashboard.")
    
# =========================
# RISK ENGINE
# =========================
with tab2:

    st.subheader("Risk Engine (Rule-Based)")

    property_id = st.text_input("Property ID")
    amount = st.number_input("Transaction Amount", min_value=0)

    risk_score = None
    status = None

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

        st.success("✅ Compliance case created successfully")

    if risk_score is not None:

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Risk Score", f"{risk_score}/100")

        with col2:
            st.metric("Risk Level", status)

        if risk_score >= 70:
            st.warning("High-risk transaction detected. Review is recommended.")
        else:
            st.info("Transaction is currently assessed as low risk.")

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
            "Risk Level",
            ["ALL", "HIGH", "LOW"]
        )

        case_filter = col2.selectbox(
            "Case Status",
            ["ALL", "OPEN", "REVIEWING", "CLOSED"]
        )

        min_risk = st.slider(
            "Minimum Risk Score",
            min_value=0,
            max_value=100,
            value=0
        )

        # Apply filters safely
        if status_filter != "ALL":
            df = df[df["Status"] == status_filter]

        if case_filter != "ALL":
            df = df[df["Case Status"] == case_filter]

        df = df[df["Risk Score"] >= min_risk]

        search = st.text_input(
            "Search Property ID",
            placeholder="Enter Property ID..."
        )

        if search:
            df = df[
                df["Property"].astype(str).str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        selected_case = st.selectbox(
            "Select Case",
            df["ID"].tolist()
        )
        
if st.button("Generate Compliance Report"):

    selected = df[df["ID"] == selected_case].iloc[0]

    report = f"""
AUSTRAC COMPLIANCE REPORT

Case ID: {selected['ID']}
Property: {selected['Property']}
Transaction Amount: ${selected['Amount']:,.2f}
Risk Score: {selected['Risk Score']}
Risk Level: {selected['Status']}
Case Status: {selected['Case Status']}

Compliance Assessment

This transaction has been automatically assessed by the AUSTRAC Risk Engine.

The calculated risk score indicates that this transaction should be reviewed in accordance with the organisation's AML/CTF compliance procedures.

Recommendation:
Conduct Enhanced Customer Due Diligence where appropriate and consider whether an SMR is required.

Generated automatically by the AUSTRAC Compliance SaaS Platform.
"""

    save_report(
        selected["ID"],
        selected["Property"],
        report
    )

    st.success("Compliance report generated.")

    st.text_area(
        "Compliance Report",
        report,
        height=350
    )

    reports = get_reports(selected["ID"])

    if reports:
        st.subheader("Previous Reports")

        for i, r in enumerate(reports, start=1):
            with st.expander(f"Report {i} - {r[4] if len(r) > 4 else 'Saved'}"):
                st.text(r[3] if len(r) > 3 else r[2])

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
    "© 2026 AUSTRAC Compliance SaaS Platform | Commercial Edition v2.0"
)
