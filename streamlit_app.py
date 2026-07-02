import streamlit as st

from pages.dashboard import show_dashboard
from pages.risk_engine import show_risk_engine
from pages.case_management import show_case_management
from utils.db import init_reports_table

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC Compliance SaaS Platform",
    layout="wide"
)

# =========================
# INITIALISE DATABASE TABLES
# =========================
init_reports_table()

# =========================
# HEADER WITH LOGO
# =========================

col1, col2 = st.columns([1, 6])

with col1:
    st.image("assets/logo.png", width=80)

with col2:
    st.title("AUSTRAC Compliance SaaS Platform")
    st.caption("Compliance Risk & Reporting System")

st.markdown("---")

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Risk Engine",
        "Case Management"
    ]
)

# =========================
# ROUTER
# =========================
if page == "Dashboard":
    show_dashboard()

elif page == "Risk Engine":
    show_risk_engine()

elif page == "Case Management":
    show_case_management()
