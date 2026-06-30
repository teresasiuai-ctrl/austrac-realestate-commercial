import streamlit as st
import os
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC Compliance Platform",
    layout="wide"
)

# =========================
# LOAD LOGO
# =========================
logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
logo = Image.open(logo_path)

# =========================
# SESSION STATE
# =========================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =========================
# AUTH FUNCTION (DEMO)
# =========================
def authenticate(username, password):
    return username == "admin" and password == "admin"

# =========================
# HEADER (NO SIDEBAR)
# =========================
col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo, width=120)

with col2:
    st.title("AUSTRAC Compliance Intelligence Platform")
    st.caption("AML / CTF Risk Monitoring System")

st.divider()

# =========================
# LOGIN PAGE
# =========================
if not st.session_state.authenticated:

    st.subheader("🔐 Login Required")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid credentials (use admin / admin)")

    st.stop()

# =========================
# MAIN APP (AFTER LOGIN)
# =========================
st.success(f"Logged in as {st.session_state.username}")

# =========================
# TABS NAVIGATION (NO SIDEBAR)
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["Dashboard", "Run Check", "Reports", "Settings"]
)

# =========================
# DASHBOARD
# =========================
with tab1:
    st.subheader("📊 Dashboard Overview")

    colA, colB, colC = st.columns(3)

    colA.metric("High Risk Alerts", "12")
    colB.metric("Properties Flagged", "5")
    colC.metric("Transactions Reviewed", "128")

    st.write("Real-time compliance monitoring dashboard.")

# =========================
# RUN CHECK
# =========================
with tab2:
    st.subheader("🔍 Run Compliance Check")

    property_id = st.text_input("Property ID")
    amount = st.number_input("Transaction Amount", min_value=0)

    if st.button("Run Analysis"):
        st.info("Running AML / CTF risk model...")
        st.success("Analysis complete (mock result)")
        st.write("Risk Score: 78/100 (High Risk)")

# =========================
# REPORTS
# =========================
with tab3:
    st.subheader("📄 Reports")

    st.write("Generated compliance reports will appear here.")

    st.button("Generate Report")

# =========================
# SETTINGS
# =========================
with tab4:
    st.subheader("⚙️ Settings")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
