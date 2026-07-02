import streamlit as st
import pandas as pd
from utils.db import get_cases


def show_dashboard():

    st.title("Compliance Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No data available yet.")
        return

    # =============================
    # DATAFRAME
    # =============================
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

    st.markdown("---")

    # =============================
    # EXECUTIVE KPI SECTION
    # =============================
    st.subheader("Executive Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Cases", len(df))
        st.metric("High Risk Cases", len(df[df["Risk Level"] == "HIGH"]))

    with col2:
        st.metric("Escalated Cases", len(df[df["Status"] == "ESCALATED"]))
        st.metric("Filed Cases", len(df[df["Status"] == "FILED"]))

    st.markdown("---")

    # =============================
    # RISK ANALYSIS
    # =============================
    st.subheader("Risk Analysis")

    risk_counts = df["Risk Level"].value_counts()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("Risk Breakdown")
        st.dataframe(risk_counts)

    with col2:
        st.bar_chart(risk_counts)

    st.markdown("---")

    # =============================
    # CASE STATUS ANALYSIS
    # =============================
    st.subheader("Case Status Breakdown")

    status_counts = df["Status"].value_counts()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("Status Summary")
        st.dataframe(status_counts)

    with col2:
        st.bar_chart(status_counts)

    st.markdown("---")

    # =============================
    # RISK SCORE DISTRIBUTION
    # =============================
    st.subheader("Risk Score Distribution")

    st.line_chart(df["Risk Score"])

    st.markdown("---")

    # =============================
    # TABLE VIEW
    # =============================
    st.subheader("All Compliance Cases")

    st.dataframe(df, use_container_width=True)
