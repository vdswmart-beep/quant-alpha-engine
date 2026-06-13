import streamlit as st
import pandas as pd

st.title("🚨 Alerts")

df = pd.read_csv(
    "outputs/alerts.csv"
)

critical = len(
    df[
        df["severity"] == "HIGH"
    ]
)

st.metric(
    "Critical Alerts",
    critical
)

st.dataframe(df)