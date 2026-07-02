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
    # Safety check (15-column DB expected)
    # -----------------------------
    if any(len(c) != 15 for c in cases):
        st.error("Database schema mismatch detected.")
        st.write(cases)
        return

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------
    df = pd.DataFrame(cases, columns=[
        "ID",
        "Property",
        "Amount",
        "Customer Name",
        "Ownership Type",
        "Funding Source",
        "Flag 1",
        "Flag 2",
        "Flag 3",
        "Flag 4",
        "Risk Score",
        "Risk Level",
        "Created",
        "User",
        "Status"
    ])

    # -----------------------------
    # Sidebar Filters
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

    # Apply filters
    filtered_df = df.copy()

    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status_filter]

    if risk_filter != "All":
        filtered_df = filtered_df[filtered_df["Risk Level"] == risk_filter]

    # -----------------------------
    # Styling helpers
    # -----------------------------
    def highlight_risk(val):
        if val == "HIGH":
            return "background-color: #ffcccc"
        elif val == "MEDIUM":
            return "background-color: #fff2cc"
        elif val == "LOW":
            return "background-color: #d9ead3"
        return ""

    def highlight_status(val):
        if val == "OPEN":
            return "font-weight: bold"
        return ""

    styled_df = filtered_df.style.applymap(
        highlight_risk,
        subset=["Risk Level"]
    ).applymap(
        highlight_status,
        subset=["Status"]
    )

    # -----------------------------
    # KPIs
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Open Cases", len(df[df["Status"] == "OPEN"]))

    st.markdown("---")

    # -----------------------------
    # Table
    # -----------------------------
    st.dataframe(styled_df, use_container_width=True)
