import streamlit as st

from models.scenarios import calculate_risk
from models.customer_due_diligence import check_cdd
from utils.db import add_case, log_action


def show_risk_engine():

    st.title("AUSTRAC Risk Engine")

    property_id = st.text_input("Property Address / ID")

    buyer_name = st.text_input("Buyer Name")

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        step=1000.0
    )

    buyer_type = st.selectbox(
        "Buyer Type",
        [
            "Individual",
            "Company",
            "Trust"
        ]
    )

    source_of_funds = st.selectbox(
        "Source of Funds",
        [
            "Employment Income",
            "Savings",
            "Business Income",
            "Inheritance",
            "Gift",
            "Loan",
            "Overseas Funds",
            "Other"
        ]
    )

    cash_payment = st.checkbox("Cash payment involved")

    overseas_funds = st.checkbox("Overseas source of funds")

    pep = st.checkbox("Politically Exposed Person (PEP)")

    sanctions = st.checkbox("Potential sanctions match")

    if st.button("Assess Risk"):

        data = {
            "amount": amount,
            "buyer_type": buyer_type,
            "cash_payment": cash_payment,
            "overseas_funds": overseas_funds,
            "pep": pep,
            "sanctions": sanctions
        }

        issues = check_cdd({
            "buyer_name": buyer_name,
            "property": property_id,
            "amount": amount,
            "source_of_funds": source_of_funds,
            "pep": pep,
            "sanctions": sanctions
        })

        score, level, reasons = calculate_risk(data)

        if issues:
            st.warning("Customer Due Diligence Issues")

            for issue in issues:
                st.write(f"• {issue}")

        st.metric("Risk Score", score)

        st.write("Risk Level:", level)

        st.subheader("Risk Factors")

        for reason in reasons:
            st.write(f"• {reason}")

try:
    add_case(
        property_id,
        amount,
        buyer_name,
        buyer_type,
        source_of_funds,
        cash_payment,
        overseas_funds,
        pep,
        sanctions,
        score,
        level,
        "admin"
    )

    st.success("Case created successfully.")

except Exception as e:
    st.error(f"Database Error: {e}")
