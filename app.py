import streamlit as st

st.set_page_config(page_title="Welcome", layout="centered")

st.title("📊 Streamlit Multi-Page Demo")
st.subheader("Welcome to the Dashboard")

st.write("""
This is the main page of your Streamlit app. Use the sidebar to navigate to:
- **Data Explorer**: Upload and preview CSV files.
- **Charts**: Visualize selected columns from the uploaded CSV.
""")
