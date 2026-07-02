import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
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

    st.dataframe(df, use_container_width=True)
