import streamlit as st

st.title("AUSTRAC Real Estate AI Agent")
st.subheader("Compliance Risk Scoring Engine")

user_input = st.text_area("Enter property / transaction details")

def risk_score(text):
    text = text.lower()

    score = 0
    flags = []

    # Basic AUSTRAC risk indicators
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
        flags.append("Urgent transaction pressure")

    if "multiple deposits" in text:
        score += 25
        flags.append("Split / structured payments risk")

    # Final classification
    if score >= 50:
        level = "HIGH RISK"
    elif score >= 20:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return score, level, flags

if st.button("Run Risk Analysis"):
    score, level, flags = risk_score(user_input)

    st.write("### Result")
    st.write("Risk Score:", score)
    st.write("Risk Level:", level)

    if flags:
        st.write("### Flags Detected")
        for f in flags:
            st.write("-", f)
    else:
        st.write("No major risk indicators detected.")
