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

    total_cases = len(df)
    high_risk = len(df[df["Risk Score"] > 70])
    open_cases = len(df[df["Case Status"] == "OPEN"])
    total_amount = df["Amount"].sum()

    st.metric("Total Cases", total_cases)
    st.metric("High Risk Cases", high_risk)
    st.metric("Open Cases", open_cases)
    st.metric("Total Amount", f"${total_amount:,.2f}")

    st.dataframe(df, use_container_width=True)
