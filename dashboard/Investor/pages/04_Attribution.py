import streamlit as st
import pandas as pd
import plotly.express as px

from shared.reports import load_strategy_results

st.title("🧩 Attribution")

df = load_strategy_results()

numeric_cols = [
    "return",
    "sharpe",
    "sortino",
    "calmar",
    "hit_ratio",
    "drawdown",
    "stability",
    "score"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

fig = px.pie(
    df,
    values="return",
    names="strategy"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.dataframe(
    df,
    width="stretch"
)