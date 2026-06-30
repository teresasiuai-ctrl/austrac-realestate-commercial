import streamlit as st
from PIL import Image
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Compliance Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD LOGO
# =========================
logo = Image.open("assets/logo.png")

# =========================
# SESSION STATE (MOCK LOGIN)
# =========================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =========================
# AUTH FUNCTION (TEMP)
# =========================
def authenticate(username, password):
    return username == "admin" and password == "admin"

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.image(logo, use_container_width=True)
    st.markdown("### Compliance Intelligence Platform")
    st.markdown("---")

    if not st.session_state.authenticated:
        st.title("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success("Login successful")
            else:
                st.error("Invalid credentials")

    else:
        st.success(f"Logged in as {st.session_state.username}")

        page = st.radio(
            "Navigation",
            ["Dashboard", "Run Check", "Reports", "Settings"]
        )

        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.rerun()

# =========================
# LOGIN GATE
# =========================
if not st.session_state.authenticated:
    st.title("📊 Compliance Intelligence Platform")
    st.write("Secure login required to access the system.")
    st.stop()

# =========================
# PAGES
# =========================
def dashboard():
    st.title("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Active Checks", "12", "+2")
    col2.metric("Risk Alerts", "3", "-1")
    col3.metric("Reports", "48", "+5")

    st.divider()

    st.info("System operational. No critical issues detected.")

def run_check():
    st.title("🧠 Run Compliance Check")

    with st.form("check_form"):
        address = st.text_input("Property Address")
        amount = st.number_input("Transaction Amount", min_value=0)
        country = st.text_input("Country")
        submit = st.form_submit_button("Run Analysis")

    if submit:
        st.info("Running analysis...")

        risk_score = min(100, int(amount / 1000))

        st.metric("Risk Score", f"{risk_score}/100")

        if risk_score > 70:
            st.error("High Risk Transaction")
        elif risk_score > 40:
            st.warning("Medium Risk Transaction")
        else:
            st.success("Low Risk Transaction")

def reports():
    st.title("📄 Reports")

    sample = [
        {"id": "RPT-001", "status": "Complete"},
        {"id": "RPT-002", "status": "Pending"}
    ]

    for r in sample:
        st.write(f"{r['id']} — {r['status']}")

def settings():
    st.title("⚙️ Settings")

    st.text_input("Organisation Name", "My Company")
    st.checkbox("Enable AI Analysis", value=True)

    st.success("Settings saved automatically")

# =========================
# ROUTER
# =========================
if page == "Dashboard":
    dashboard()
elif page == "Run Check":
    run_check()
elif page == "Reports":
    reports()
elif page == "Settings":
    settings()

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption(f"© {datetime.now().year} Compliance Intelligence Platform")
