import streamlit as st
import pandas as pd

st.title("📝 Orders")

df = pd.read_csv(
    "outputs/orders.csv"
)

st.metric(
    "Total Orders",
    len(df)
)

st.dataframe(df)