import streamlit as st

st.title("AUSTRAC Real Estate AI Agent")

st.write("Commercial Compliance Dashboard (MVP)")

user_input = st.text_area("Enter property / transaction data")

if st.button("Run Compliance Check"):
    st.write("Analysis Result")
    st.write({
        "status": "received",
        "input": user_input,
        "result": "placeholder - AI not connected yet"
    })
