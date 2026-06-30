import streamlit as st
import json

st.set_page_config(
    page_title="AUSTRAC Compliance Platform",
    page_icon="🏠",
    layout="wide"
)

# Header
st.title("🏠 AUSTRAC Real Estate Compliance Platform")
st.caption("Commercial-grade compliance risk analysis tool (MVP)")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Transaction Input")
    bulk_input = st.text_area(
        "Enter transactions (one per line)",
        height=250
    )

    run = st.button("Run Compliance Analysis")

with col2:
    st.subheader("System Status")
    st.success("Online")
    st.info("Rule Engine Active")
    st.warning("No AI API connected (free mode)")

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
        level = "🔴 HIGH RISK"
    elif score >= 20:
        level = "🟠 MEDIUM RISK"
    else:
        level = "🟢 LOW RISK"

    return score, level, flags


if run:
    if not bulk_input.strip():
        st.warning("Please enter transactions")
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
            with st.expander(f"Transaction {r['id']} - {r['level']}"):
                st.write("Input:", r["input"])
                st.write("Score:", r["score"])
                st.write("Flags:", r["flags"])

        st.download_button(
            "Download Full Report",
            json.dumps(results, indent=2),
            file_name="austrac_report.json",
            mime="application/json"
        )
