import streamlit as st
import pandas as pd
from utils.db import get_cases


def show_dashboard():

    st.title("Compliance Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No data available yet.")
        return

    df = pd.DataFrame(cases, columns=[
        "ID",
        "Property",
        "Amount",
        "Buyer Name",
        "Buyer Type",
        "Source of Funds",
        "Cash Payment",
        "Overseas Funds",
        "PEP",
        "Sanctions",
        "Risk Score",
        "Risk Level",
        "Status"
    ])

    # =============================
    # KPI SECTION
    # =============================
    st.subheader("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Escalated", len(df[df["Status"] == "ESCALATED"]))
    col4.metric("Filed", len(df[df["Status"] == "FILED"]))

    st.markdown("---")

    # =============================
    # RISK LEVEL DISTRIBUTION
    # =============================
    st.subheader("Risk Level Distribution")

    risk_counts = df["Risk Level"].value_counts()
    st.bar_chart(risk_counts)

    # =============================
    # CASE STATUS BREAKDOWN
    # =============================
    st.subheader("Case Status Breakdown")

    status_counts = df["Status"].value_counts()
    st.bar_chart(status_counts)

    # =============================
    # RISK SCORE INSIGHT
    # =============================
    st.subheader("Risk Score Overview")

    st.line_chart(df["Risk Score"])

    # =============================
    # RAW TABLE
    # =============================
    st.markdown("---")
    st.subheader("All Cases")

    st.dataframe(df, use_container_width=True)
