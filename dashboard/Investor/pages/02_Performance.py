import streamlit as st
import pandas as pd
import plotly.express as px

from shared.reports import load_portfolio

st.set_page_config(
    page_title="Performance",
    layout="wide"
)

st.title("📊 Performance")

portfolio = load_portfolio()

equity = portfolio["equity"]

returns = equity.pct_change().fillna(0)

monthly = (
    returns
    .resample("ME")
    .sum()
)

monthly_df = pd.DataFrame(
    {
        "Month": monthly.index,
        "Return": monthly.values
    }
)

fig = px.bar(
    monthly_df,
    x="Month",
    y="Return",
    title="Monthly Performance"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    monthly_df,
    width="stretch"
)