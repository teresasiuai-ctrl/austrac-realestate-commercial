import streamlit as st
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Compliance Platform",
    page_icon="📊",
    layout="wide"
)

# =========================
# SIMPLE SESSION STATE (MOCK LOGIN)
# =========================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =========================
# MOCK AUTH FUNCTION
# =========================
def authenticate(username, password):
    # Replace later with real auth system (Firebase / Supabase / etc.)
    return username == "admin" and password == "admin"

# =========================
# SIDEBAR LOGIN / NAV
# =========================
with st.sidebar:
    st.title("🔐 Access Portal")

    if not st.session_state.authenticated:
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
    st.write("Secure access required to continue.")
    st.stop()

# =========================
# CORE PAGES
# =========================

def dashboard():
    st.title("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Active Checks", "12", "+2 today")
    col2.metric("Risk Alerts", "3", "-1 today")
    col3.metric("Reports Generated", "48", "+5 this week")

    st.divider()

    st.subheader("System Overview")
    st.info("All systems operational. No critical compliance failures detected.")

def run_check():
    st.title("🧠 Run Compliance Check")

    st.write("Enter property / transaction data below:")

    with st.form("check_form"):
        address = st.text_input("Property Address")
        amount = st.number_input("Transaction Amount", min_value=0)
        country = st.text_input("Country")
        submit = st.form_submit_button("Run Analysis")

    if submit:
        st.info("Running AI compliance analysis...")

        # Placeholder logic (replace with AI model later)
        risk_score = min(100, int(amount / 1000))

        st.success("Analysis Complete")

        st.metric("Risk Score", f"{risk_score}/100")

        if risk_score > 70:
            st.error("High Risk Transaction Detected")
        elif risk_score > 40:
            st.warning("Medium Risk - Review Required")
        else:
            st.success("Low Risk Transaction")

def reports():
    st.title("📄 Reports")

    st.write("Generated reports will appear here.")

    sample_reports = [
        {"id": "RPT-001", "date": "2026-06-30", "status": "Complete"},
        {"id": "RPT-002", "date": "2026-06-29", "status": "Pending"},
    ]

    for r in sample_reports:
        st.write(f"**{r['id']}** | {r['date']} | {r['status']}")

def settings():
    st.title("⚙️ Settings")

    st.text_input("Organisation Name", value="My Company")
    st.text_input("API Key (future integration)")
    st.checkbox("Enable AI auto-analysis", value=True)

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
st.caption(f"© {datetime.now().year} Compliance Intelligence Platform | Secure SaaS Build")
