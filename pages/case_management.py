import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
        return

    cleaned_cases = []

    for c in cases:

        # Your actual DB format (15 columns)
        if isinstance(c, (list, tuple)) and len(c) >= 15:

            cleaned_cases.append([
                c[0],   # ID
                c[1],   # Property
                c[2],   # Amount
                c[3],   # Customer Name
                c[4],   # Ownership Type
                c[5],   # Funding Source
                c[10],  # Risk Score
                c[11],  # Risk Level
                c[12],  # Created
                c[13],  # User
                c[14],  # Status
            ])

        else:
            continue

    if not cleaned_cases:
        st.warning("Data format mismatch. Raw output below:")
        st.write(cases)
        return

    df = pd.DataFrame(cleaned_cases, columns=[
        "ID",
        "Property",
        "Amount",
        "Customer Name",
        "Ownership Type",
        "Funding Source",
        "Risk Score",
        "Risk Level",
        "Created",
        "User",
        "Status"
    ])

    st.dataframe(df, use_container_width=True)
