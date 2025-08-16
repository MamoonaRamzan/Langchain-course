import streamlit as st
import requests

# Backend URL
BASE_URL = "http://localhost:8000"

st.title("🌟 LangChain AI Frontend")

# Select endpoint
endpoint = st.selectbox(
    "Choose an endpoint:",
    ["groqai", "essay", "poem"]
)

# Input box
user_input = st.text_area("Enter your input:")

# Button to send request
if st.button("Generate"):
    try:
        if endpoint == "groqai":
            payload = {"input": user_input}  # direct string
        else:
            payload = {"input": {"topic": user_input}}  # dictionary with topic

        # POST request
        response = requests.post(f"{BASE_URL}/{endpoint}/invoke", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Response:")
            st.write(result.get("output"))
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"⚠️ Request failed: {str(e)}")
