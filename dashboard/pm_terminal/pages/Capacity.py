import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏦 Capacity Analysis")

df = pd.read_csv(
    "outputs/capacity_report.csv"
)

st.dataframe(df)

fig = px.bar(
    df,
    x="strategy",
    y="capacity"
)

st.plotly_chart(
    fig,
    use_container_width=True
)