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
    # Normalize incoming data safely
    # -----------------------------
    cleaned_cases = []

    for c in cases:

        # Case 1: dictionary format
        if isinstance(c, dict):
            cleaned_cases.append([
                c.get("id"),
                c.get("property"),
                c.get("amount"),
                c.get("risk_score"),
                c.get("status"),
                c.get("created"),
                c.get("user"),
                c.get("case_status"),
            ])

        # Case 2: tuple/list with correct length
        elif isinstance(c, (list, tuple)) and len(c) == 8:
            cleaned_cases.append(list(c))

        # Case 3: broken row (skip it safely)
        else:
            continue

    # If everything got filtered out
    if not cleaned_cases:
        st.warning("Cases exist but data format is invalid. Check database output.")
        st.write(cases)
        return

    # -----------------------------
    # Build DataFrame safely
    # -----------------------------
    df = pd.DataFrame(cleaned_cases, columns=[
        "ID",
        "Property",
        "Amount",
        "Risk Score",
        "Status",
        "Created",
        "User",
        "Case Status"
    ])

    # -----------------------------
    # Display table
    # -----------------------------
    st.dataframe(df, use_container_width=True)
