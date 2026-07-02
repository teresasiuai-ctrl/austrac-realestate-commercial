import streamlit as st
import pandas as pd
from utils.db import get_cases


def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
        return

    # =========================
    # SAFE DATAFRAME (NO CRASH MODE)
    # =========================
    df = pd.DataFrame(cases)

    # Ensure minimum structure exists
    if df.shape[1] < 13:
        st.error("Database schema mismatch detected. Please reset or migrate DB.")
        st.write(df)
        return

    # Normalize to expected schema
    df = df.iloc[:, :13]

    df.columns = [
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
    ]

    # =========================
    # CASE TABLE
    # =========================
    st.subheader("All Cases")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    # =========================
    # CASE SELECTOR
    # =========================
    selected_id = st.selectbox("Select Case ID", df["ID"].tolist())

    case = df[df["ID"] == selected_id].iloc[0]

    # =========================
    # CASE DETAILS
    # =========================
    st.subheader("Case Details")

    st.write(f"**Property:** {case['Property']}")
    st.write(f"**Amount:** ${case['Amount']}")
    st.write(f"**Buyer Name:** {case['Buyer Name']}")
    st.write(f"**Buyer Type:** {case['Buyer Type']}")
    st.write(f"**Source of Funds:** {case['Source of Funds']}")
    st.write(f"**Cash Payment:** {case['Cash Payment']}")
    st.write(f"**Overseas Funds:** {case['Overseas Funds']}")
    st.write(f"**PEP:** {case['PEP']}")
    st.write(f"**Sanctions:** {case['Sanctions']}")
    st.write(f"**Risk Score:** {case['Risk Score']}")
    st.write(f"**Risk Level:** {case['Risk Level']}")
    st.write(f"**Status:** {case['Status']}")
