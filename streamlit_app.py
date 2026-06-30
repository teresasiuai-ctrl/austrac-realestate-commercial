import streamlit as st

st.set_page_config(
    page_title="AUSTRAC Compliance Checker",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AUSTRAC Real Estate Compliance Checker")
st.write("Free tool to identify basic transaction risk indicators (educational use only).")

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
        flags.append("Structured / split payments risk")

    if score >= 50:
        level = "🔴 HIGH RISK"
    elif score >= 20:
        level = "🟠 MEDIUM RISK"
    else:
        level = "🟢 LOW RISK"

    return score, level, flags

if st.button("Check Risk"):
    if not user_input.strip():
        st.warning("Please enter transaction details.")
    else:
        score, level, flags = risk_score(user_input)

        st.subheader("Result")
        st.write("Risk Level:", level)
        st.write("Risk Score:", score)

        if flags:
            st.subheader("Flags Detected")
            for f in flags:
                st.write("•", f)
        else:
            st.success("No major risk indicators detected.")

st.caption("⚠️ This tool is for educational and compliance support only. Not legal advice.")
