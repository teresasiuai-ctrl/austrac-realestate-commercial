import streamlit as st
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Batch Checker",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 AUSTRAC Batch Compliance Checker")

st.write("Paste multiple transactions (one per line)")

bulk_input = st.text_area("Transactions")

def analyze(text):
    text = text.lower()

    score = 0
    flags = []

    if "cash" in text:
        score += 30
        flags.append("Cash transaction")

    if "offshore" in text:
        score += 25
        flags.append("Offshore involvement")

    if "third party" in text:
        score += 20
        flags.append("Third-party payment")

    if "urgent" in text:
        score += 10
        flags.append("Urgency pressure")

    if "multiple deposits" in text:
        score += 25
        flags.append("Structured payments")

    if score >= 50:
        level = "HIGH"
    elif score >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, flags


if st.button("Run Batch Analysis"):
    if not bulk_input.strip():
        st.warning("Enter transactions first")
    else:
        lines = bulk_input.strip().split("\n")

        results = []

        for i, line in enumerate(lines, start=1):
            score, level, flags = analyze(line)

            results.append({
                "id": i,
                "input": line,
                "score": score,
                "level": level,
                "flags": flags
            })

        st.subheader("Results")

        for r in results:
            st.write(r)

        st.download_button(
            "Download Batch Report",
            json.dumps(results, indent=2),
            file_name="batch_austrac_report.json",
            mime="application/json"
        )
