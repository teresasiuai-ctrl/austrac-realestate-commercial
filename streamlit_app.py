import streamlit as st

from pages.dashboard import show_dashboard
from pages.risk_engine import show_risk_engine
from pages.case_management import show_case_management

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC Compliance SaaS Platform",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("AUSTRAC Compliance SaaS Platform")

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
