import streamlit as st
import pandas as pd

st.title("🧮 Data Explorer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.subheader("Preview of your data:")
    st.dataframe(df)
else:
    st.info("Please upload a CSV file to begin.")
