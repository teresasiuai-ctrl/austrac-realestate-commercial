import streamlit as st
import pandas as pd
import io

from utils.db import get_cases, save_report, get_reports_by_case
from models.compliance_report import generate_smr_report

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def show_case_management():

    st.title("Case Management")

    cases = get_cases()

    if not cases:
        st.info("No cases found.")
        return

    # -----------------------------
    # SCHEMA VALIDATION (8 columns)
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
    # FILTERS
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
    # KPI DASHBOARD
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Cases", len(df))
    col2.metric("High Risk", len(df[df["Risk Level"] == "HIGH"]))
    col3.metric("Open Cases", len(df[df["Status"] == "OPEN"]))

    st.markdown("---")

    # -----------------------------
    # CASE SELECTION (NEW)
    # -----------------------------
    st.subheader("Select Case")

    case_options = {
        f"{row[0]} | {row[1]} | ${row[2]} | {row[4]}": row
        for row in cases
    }

    selected_label = st.selectbox(
        "Choose a case to review",
        list(case_options.keys())
    )

    selected_case = case_options[selected_label]
    case_id = selected_case[0]

    st.markdown("---")

    # -----------------------------
    # CASE DETAILS
    # -----------------------------
    st.subheader("Case Details")

    st.write(f"Property: {selected_case[1]}")
    st.write(f"Amount: ${selected_case[2]}")
    st.write(f"Risk Score: {selected_case[3]}")
    st.write(f"Risk Level: {selected_case[4]}")
    st.write(f"Status: {selected_case[7]}")

    # -----------------------------
    # GENERATE REPORT
    # -----------------------------
    if st.button("Generate Compliance Report"):

        report = generate_smr_report(selected_case)

        save_report(case_id, report)

        st.success("Compliance report generated and saved.")

    # -----------------------------
    # LOAD REPORTS
    # -----------------------------
    reports = get_reports_by_case(case_id)

    if reports:

        latest_report = reports[0][1]

        st.subheader("Latest Compliance Report")

        with st.expander("View Report"):
            st.text(latest_report)

        # -----------------------------
        # DOWNLOAD PDF
        # -----------------------------
        if st.button("Download PDF"):

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)

            styles = getSampleStyleSheet()
            content = []

            for line in latest_report.split("\n"):
                content.append(Paragraph(line, styles["Normal"]))
                content.append(Spacer(1, 6))

            doc.build(content)

            st.download_button(
                "Download Report PDF",
                buffer.getvalue(),
                file_name=f"case_{case_id}_compliance_report.pdf",
                mime="application/pdf"
            )

    else:
        st.info("No compliance report generated yet for this case.")

    # -----------------------------
    # FULL TABLE VIEW (existing feature)
    # -----------------------------
    st.markdown("---")
    st.subheader("All Cases")

    st.dataframe(filtered_df, use_container_width=True)
