import streamlit as st
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Checker",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AUSTRAC Real Estate Compliance AI")

user_input = st.text_area("Enter property or transaction details")

def analyze(text):
    text = text.lower()

    score = 0
    flags = []
    explanation = []

    if "cash" in text:
        score += 30
        flags.append("Cash transaction detected")
        explanation.append("Cash transactions increase money laundering risk due to reduced traceability.")

    if "offshore" in text:
        score += 25
        flags.append("Offshore involvement")
        explanation.append("Offshore entities may increase AML/CTF complexity.")

    if "third party" in text:
        score += 20
        flags.append("Third-party payment")
        explanation.append("Third-party payments can obscure beneficial ownership.")

    if "urgent" in text:
        score += 10
        flags.append("Urgency pressure")
        explanation.append("Urgency may indicate attempt to bypass due diligence.")

    if "multiple deposits" in text:
        score += 25
        flags.append("Structured payments")
        explanation.append("Split payments may indicate structuring to avoid detection thresholds.")

    if score >= 50:
        level = "🔴 HIGH RISK"
    elif score >= 20:
        level = "🟠 MEDIUM RISK"
    else:
        level = "🟢 LOW RISK"

    return score, level, flags, explanation


if st.button("Run Analysis"):
    if not user_input.strip():
        st.warning("Please enter details")
    else:
        score, level, flags, explanation = analyze(user_input)

        result = {
            "risk_score": score,
            "risk_level": level,
            "flags": flags,
            "explanation": explanation
        }

        st.subheader("Result")
        st.write("Risk Level:", level)
        st.write("Risk Score:", score)

        st.subheader("Flags")
        for f in flags:
            st.write("•", f)

        st.subheader("AI Explanation")
        for e in explanation:
            st.write("•", e)

        st.download_button(
            "Download Report",
            json.dumps(result, indent=2),
            file_name="austrac_report.json",
            mime="application/json"
        )
