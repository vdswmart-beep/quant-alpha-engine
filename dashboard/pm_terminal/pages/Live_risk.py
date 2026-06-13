import streamlit as st
import pandas as pd

st.title(
    "Live Risk Monitor"
)

risk = pd.read_csv(
    "outputs/live_risk.csv"
)

st.dataframe(risk)