import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_dashboard():

    st.title("Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No cases yet.")
        return

    df = pd.DataFrame(
        cases,
        columns=[
            "ID",
            "Property",
            "Amount",
            "Risk Score",
            "Status",
            "Created",
            "User",
            "Case Status"
        ]
    )

    # =========================
    # KPI METRICS
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Score"] > 70]))
    col3.metric("Open Cases", len(df[df["Case Status"] == "OPEN"]))
    col4.metric("Total Amount", f"${df['Amount'].sum():,.2f}")

    st.divider()

    st.subheader("Recent Cases")
    st.dataframe(df, use_container_width=True)
