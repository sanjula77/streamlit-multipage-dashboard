import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Chart Visualizer")

uploaded_file = st.file_uploader("Upload the same or another CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Select a column to visualize")

    column = st.selectbox("Select column", df.columns)

    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind='bar', ax=ax, color='skyblue')
    plt.title(f"Distribution of {column}")
    st.pyplot(fig)
else:
    st.info("Please upload a CSV file.")
