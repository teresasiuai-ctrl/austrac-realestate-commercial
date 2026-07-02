import streamlit as st
import pandas as pd
from utils.db import get_cases


def show_dashboard():

    st.title("Compliance Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No data available yet.")
        return

    # SAFE: auto-handle row length (prevents blank screen crashes)
    df = pd.DataFrame(cases)

    # Rename only if expected structure exists
    if df.shape[1] >= 13:
        df = df.iloc[:, :13]
        df.columns = [
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
        ]
    else:
        st.warning("Database schema mismatch detected")
        st.dataframe(df)
        return

    # =========================
    # KPI SECTION
    # =========================
    st.subheader("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Escalated", len(df[df["Status"] == "ESCALATED"]))
    col4.metric("Filed", len(df[df["Status"] == "FILED"]))

    st.markdown("---")

    # =========================
    # RISK ANALYSIS
    # =========================
    st.subheader("Risk Level Distribution")
    st.bar_chart(df["Risk Level"].value_counts())

    st.subheader("Case Status Breakdown")
    st.bar_chart(df["Status"].value_counts())

    st.subheader("Risk Score Overview")
    st.line_chart(df["Risk Score"])

    st.markdown("---")

    st.subheader("All Cases")
    st.dataframe(df, use_container_width=True)
