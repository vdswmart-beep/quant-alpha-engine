import streamlit as st

from shared.reports import load_portfolio
from shared.charts import drawdown_chart

from shared.metrics import (
    max_drawdown,
    calmar_ratio
)

st.title("⚠ Risk Analytics")

portfolio = load_portfolio()

equity = portfolio["equity"]

returns = equity.pct_change().fillna(0)

peak = equity.cummax()

drawdown = equity / peak - 1

c1, c2 = st.columns(2)

c1.metric(
    "Max Drawdown",
    f"{max_drawdown(equity)*100:.2f}%"
)

c2.metric(
    "Calmar",
    f"{calmar_ratio(returns):.2f}"
)

st.plotly_chart(
    drawdown_chart(drawdown),
    width="stretch"
)