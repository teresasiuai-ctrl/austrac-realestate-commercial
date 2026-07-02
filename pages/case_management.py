import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
        return

    # -----------------------------
    # FIXED: now expecting 8 columns
    # -----------------------------
    if any(len(c) != 8 for c in cases):
        st.error("Database schema mismatch detected (expected 8 columns).")
        st.write(cases)
        return

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
    # Filters
    # -----------------------------
    st.sidebar.header("Filters")

    status_filter = st.sidebar.selectbox(
        "Status",
        ["All"] + sorted(df["Status"].dropna().unique().tolist())
    )

    risk_filter = st.sidebar.selectbox(
        "Risk Level",
        ["All"] + sorted(df["Risk Level"].dropna().unique().tolist())
    )

    filtered_df = df.copy()

    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status_filter]

    if risk_filter != "All":
        filtered_df = filtered_df[filtered_df["Risk Level"] == risk_filter]

    # -----------------------------
    # KPIs
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Open Cases", len(df[df["Status"] == "OPEN"]))

    st.markdown("---")

    # -----------------------------
    # Display
    # -----------------------------
    st.dataframe(filtered_df, use_container_width=True)
