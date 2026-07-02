import streamlit as st
import pandas as pd

from utils.db import get_cases


def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
        return

    # =============================
    # SAFE DATAFRAME (LOCKED SCHEMA)
    # =============================
    df = pd.DataFrame(cases, columns=[
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
    ])

    # =============================
    # CASE LIST VIEW
    # =============================
    st.subheader("All Cases")

    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # =============================
    # CASE SELECTION
    # =============================
    case_ids = df["ID"].tolist()

    selected_id = st.selectbox("Select Case ID", case_ids)

    selected_case = df[df["ID"] == selected_id].iloc[0]

    # =============================
    # CASE DETAILS
    # =============================
    st.subheader("Case Details")

    st.write(f"**Property:** {selected_case['Property']}")
    st.write(f"**Amount:** ${selected_case['Amount']}")
    st.write(f"**Buyer Name:** {selected_case['Buyer Name']}")
    st.write(f"**Buyer Type:** {selected_case['Buyer Type']}")
    st.write(f"**Source of Funds:** {selected_case['Source of Funds']}")
    st.write(f"**Cash Payment:** {selected_case['Cash Payment']}")
    st.write(f"**Overseas Funds:** {selected_case['Overseas Funds']}")
    st.write(f"**PEP:** {selected_case['PEP']}")
    st.write(f"**Sanctions:** {selected_case['Sanctions']}")
    st.write(f"**Risk Score:** {selected_case['Risk Score']}")
    st.write(f"**Risk Level:** {selected_case['Risk Level']}")
    st.write(f"**Status:** {selected_case['Status']}")
