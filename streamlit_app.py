import streamlit as st
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Checker",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AUSTRAC Real Estate Compliance Checker")

user_input = st.text_area("Enter property or transaction details")

def risk_score(text):
    text = text.lower()

    score = 0
    flags = []

    if "cash" in text:
        score += 30
        flags.append("Cash transaction detected")

    if "offshore" in text:
        score += 25
        flags.append("Offshore involvement")

    if "third party" in text:
        score += 20
        flags.append("Third-party payment")

    if "urgent" in text:
        score += 10
        flags.append("Urgency pressure indicator")

    if "multiple deposits" in text:
        score += 25
        flags.append("Structured payments risk")

    if score >= 50:
        level = "HIGH RISK"
    elif score >= 20:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return score, level, flags


if st.button("Check Risk"):
    if not user_input.strip():
        st.warning("Enter details first")
    else:
        score, level, flags = risk_score(user_input)

        result = {
            "input": user_input,
            "risk_score": score,
            "risk_level": level,
            "flags": flags
        }

        st.subheader("Result")
        st.write(result)

        st.download_button(
            label="Download Report (JSON)",
            data=json.dumps(result, indent=2),
            file_name="austrac_report.json",
            mime="application/json"
        )
