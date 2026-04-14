import streamlit as st
import pandas as pd
from agent import profile_data, decide_actions, apply_actions
from utils import compute_metrics, compare_metrics

st.set_page_config(page_title="AI Data Cleaning Agent", layout="wide")

st.title("🤖 AI Data Cleaning Agent")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Raw Data")
    st.dataframe(df.head())

    before_metrics = compute_metrics(df)

    if st.button("🚀 Run Agent"):

        config = {"drop_threshold": 0.3}

        profile = profile_data(df)
        decisions = decide_actions(profile, config)
        cleaned_df, logs = apply_actions(df.copy(), decisions)

        after_metrics = compute_metrics(cleaned_df)
        comparison = compare_metrics(before_metrics, after_metrics)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Before")
            st.json(before_metrics)

        with col2:
            st.subheader("📊 After")
            st.json(after_metrics)

        st.subheader("📈 Comparison")
        st.json(comparison)

        st.subheader("✅ Cleaned Data")
        st.dataframe(cleaned_df.head())

        st.subheader("🧠 Agent Logs")
        for log in logs:
            st.write("•", log)

        # Download
        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇ Download Cleaned Data",
            csv,
            "cleaned_data.csv",
            "text/csv"
        )