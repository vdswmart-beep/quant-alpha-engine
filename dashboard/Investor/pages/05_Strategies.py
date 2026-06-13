import streamlit as st
import pandas as pd

from shared.reports import load_strategy_results

st.title("📑 Strategy Tear Sheets")

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

strategy = st.selectbox(
    "Strategy",
    sorted(df["strategy"].dropna().unique())
)

row = df[
    df["strategy"] == strategy
].iloc[0]

c1, c2, c3 = st.columns(3)

c1.metric(
    "Sharpe",
    f"{row['sharpe']:.2f}"
)

c2.metric(
    "Return",
    f"{row['return']:.2f}%"
)

c3.metric(
    "Max DD",
    f"{row['drawdown']:.2%}"
)

st.dataframe(
    row.to_frame(),
    width="stretch"
)