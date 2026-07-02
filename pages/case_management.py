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
    # Safety check (prevents silent breakage)
    # -----------------------------
    if any(len(c) != 15 for c in cases):
        st.error("Database schema mismatch detected (expected 15 columns per row).")
        st.write(cases)
        return

    # -----------------------------
    # Build DataFrame (stable mapping)
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
    # Display table
    # -----------------------------
    st.dataframe(df, use_container_width=True)
