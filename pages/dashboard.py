import streamlit as st
import pandas as pd
from utils.db import get_cases

def show_dashboard():

    st.title("Compliance Dashboard")

    cases = get_cases()

    if not cases:
        st.info("No data available yet.")
        return

    # =============================
    # DATAFRAME (matches your 13-column schema)
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
    # KPIs
    # =============================
    st.subheader("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Escalated", len(df[df["Status"] == "ESCALATED"]))
    col4.metric("Filed", len(df[df["Status"] == "FILED"]))

    st.markdown("---")

    # =============================
    # RISK DISTRIBUTION
    # =============================
    st.subheader("Risk Level Distribution")

    risk_counts = df["Risk Level"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(risk_counts, labels=risk_counts.index, autopct="%1.1f%%")
    ax1.axis("equal")

    st.pyplot(fig1)

    # =============================
    # CASE STATUS BREAKDOWN
    # =============================
    st.subheader("Case Status Breakdown")

    status_counts = df["Status"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.bar(status_counts.index, status_counts.values)

    st.pyplot(fig2)

    # =============================
    # RISK SCORE INSIGHT
    # =============================
    st.subheader("Risk Score Overview")

    fig3, ax3 = plt.subplots()
    ax3.hist(df["Risk Score"], bins=10)

    st.pyplot(fig3)

    # =============================
    # RAW TABLE
    # =============================
    st.markdown("---")
    st.subheader("All Cases")

    st.dataframe(df, use_container_width=True)
