import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎲 Monte Carlo Analysis")

df = pd.read_csv(
    "outputs/monte_carlo.csv"
)

st.metric(
    "Expected Terminal Value",
    round(df["terminal_value"].mean(), 2)
)

st.metric(
    "Worst 5%",
    round(
        df["terminal_value"].quantile(0.05),
        2
    )
)

fig = px.histogram(
    df,
    x="terminal_value",
    nbins=50,
    title="Monte Carlo Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(df.head())