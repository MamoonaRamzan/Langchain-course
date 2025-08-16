import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  # FastAPI server

st.set_page_config(page_title="LangChain Streamlit Demo", page_icon="🤖", layout="centered")

st.title("LangChain + Streamlit Playground")

# Sidebar for choosing endpoint
endpoint = st.sidebar.selectbox(
    "Choose an endpoint",
    ["poem", "essay", "math"]
)

# User input
user_input = st.text_area("Enter your input:", placeholder="Type something...")

if st.button("Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter some input first.")
    else:
        url = f"{BASE_URL}/{endpoint}/invoke"
        try:
            response = requests.post(url, json={"input": user_input})
            if response.status_code == 200:
                data = response.json()
                st.success("Response:")
                st.write(data.get("output", "No output field in response"))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
