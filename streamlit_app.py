import streamlit as st
import os
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AUSTRAC Intelligence Platform",
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
# AUTH (DEMO ONLY)
# =========================
def authenticate(username, password):
    return username == "admin" and password == "admin"

# =========================
# HEADER (SAAS STYLE)
# =========================
def render_header():
    col1, col2, col3 = st.columns([1, 6, 2])

    with col1:
        st.image(logo, width=90)

    with col2:
        st.title("AUSTRAC Intelligence Platform")
        st.caption("AML / CTF Risk Monitoring & Real Estate Compliance Engine")

    with col3:
        if st.session_state.authenticated:
            st.markdown(f"👤 **{st.session_state.username}**")
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.rerun()

st.set_page_config(page_title="AUSTRAC Platform", layout="wide")

render_header()

st.divider()

# =========================
# LOGIN PAGE
# =========================
if not st.session_state.authenticated:

    st.subheader("🔐 Secure Login")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        st.caption("Demo login: admin / admin")

        if st.button("Login", use_container_width=True):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()

# =========================
# DASHBOARD TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Overview", "🔍 Risk Engine", "📄 Reports", "⚙️ Settings"]
)

# =========================
# OVERVIEW (SAAS DASHBOARD)
# =========================
with tab1:

    st.subheader("System Overview")

    colA, colB, colC, colD = st.columns(4)

    colA.metric("High Risk Alerts", "12", "+2")
    colB.metric("Properties Monitored", "540", "+18")
    colC.metric("Transactions Scanned", "1,284", "+93")
    colD.metric("Compliance Score", "87%", "+3%")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.info("📍 Live Monitoring Active")
        st.write("System is scanning real estate transactions for AML/CTF risk patterns in real time.")

    with col2:
        st.warning("⚠️ Flagged Activity Queue")
        st.write("3 new transactions require manual review.")

# =========================
# RISK ENGINE
# =========================
with tab2:

    st.subheader("Risk Analysis Engine")

    property_id = st.text_input("Property ID / Reference")
    amount = st.number_input("Transaction Amount", min_value=0)

    col1, col2 = st.columns(2)

    with col1:
        region = st.selectbox("Region", ["NSW", "VIC", "QLD", "WA", "SA"])

    with col2:
        risk_type = st.selectbox("Risk Type", ["Purchase", "Transfer", "Trust Structure", "Cash Payment"])

    if st.button("Run Compliance Check", use_container_width=True):

        st.info("Running AI risk model...")

        st.progress(80)

        st.success("Analysis Complete")

        st.markdown("### 🧠 Risk Result")
        st.error("High Risk Score: 82 / 100")

        st.write("""
        - ⚠️ Unusual transaction pattern detected  
        - ⚠️ High-risk jurisdiction mapping  
        - ⚠️ Potential structuring behavior  
        """)

# =========================
# REPORTS
# =========================
with tab3:

    st.subheader("Compliance Reports")

    st.write("Generate and export AML / CTF compliance reports.")

    col1, col2 = st.columns(2)

    with col1:
        st.button("Generate Report", use_container_width=True)

    with col2:
        st.button("Export PDF", use_container_width=True)

    st.info("No reports generated yet.")

# =========================
# SETTINGS
# =========================
with tab4:

    st.subheader("System Settings")

    st.toggle("Enable Real-Time Monitoring", value=True)
    st.toggle("Auto-Flag High Risk Transactions", value=True)

    st.selectbox("Risk Sensitivity", ["Low", "Medium", "High"])

    st.button("Save Settings", use_container_width=True)
