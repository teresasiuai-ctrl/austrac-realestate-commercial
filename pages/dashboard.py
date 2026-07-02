import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_dashboard():

    st.title("Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No cases available.")
        return

    # -----------------------------
    # SAFETY CHECK (8-column schema)
    # -----------------------------
    if any(len(c) != 8 for c in cases):
        st.error("Database schema mismatch detected (expected 8 columns).")
        st.write(cases)
        return

    # -----------------------------
    # DataFrame
    # -----------------------------
    df = pd.DataFrame(cases, columns=[
        "ID",
        "Property",
        "Amount",
        "Risk Score",
        "Risk Level",
        "Created",
        "User",
        "Status"
    ])

    # -----------------------------
    # KPIs
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Medium Risk", len(df[df["Risk Level"] == "MEDIUM"]))
    col4.metric("Open Cases", len(df[df["Status"] == "OPEN"]))

    st.markdown("---")

    # -----------------------------
    # Recent Cases
    # -----------------------------
    st.subheader("Recent Cases")
    st.dataframe(df.sort_values("Created", ascending=False), use_container_width=True)
