import streamlit as st
from utils.db import add_case, log_action

def show_risk_engine():

    st.title("Risk Engine")

    st.subheader("Create New Transaction Case")

    property_id = st.text_input("Property ID / Address")

    amount = st.number_input("Transaction Amount", min_value=0.0, step=1000.0)

    source_of_funds = st.selectbox(
        "Source of Funds",
        ["Verified Salary", "Savings", "Loan", "Unknown", "Overseas Transfer"]
    )

    buyer_type = st.selectbox(
        "Buyer Type",
        ["Individual", "Company", "Trust", "SMSF"]
    )

    cash_involved = st.checkbox("Cash involved in transaction")

    # =========================
    # SIMPLE RULE-BASED RISK ENGINE
    # =========================
    risk_score = 0

    if amount > 1000000:
        risk_score += 30

    if source_of_funds in ["Unknown", "Overseas Transfer"]:
        risk_score += 30

    if buyer_type in ["Company", "Trust", "SMSF"]:
        risk_score += 20

    if cash_involved:
        risk_score += 20

    risk_score = min(risk_score, 100)

    st.subheader("Calculated Risk Score")
    st.metric("Risk Score", risk_score)

    if risk_score >= 70:
        status = "HIGH"
        st.error("High Risk Transaction")
    elif risk_score >= 40:
        status = "MEDIUM"
        st.warning("Medium Risk Transaction")
    else:
        status = "LOW"
        st.success("Low Risk Transaction")

    # =========================
    # SAVE CASE
    # =========================
    if st.button("Create Case"):

        add_case(
            property_id,
            amount,
            risk_score,
            status,
            user="admin"
        )

        log_action("admin", f"Created case for {property_id}")

        st.success("Case created successfully")
