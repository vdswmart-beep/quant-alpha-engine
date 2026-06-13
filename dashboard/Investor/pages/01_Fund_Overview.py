import streamlit as st
import pandas as pd

from shared.reports import load_portfolio
from shared.charts import equity_curve

from shared.metrics import (
    annual_return,
    annual_volatility,
    sharpe_ratio
)

st.title("🏦 Fund Overview")

portfolio = load_portfolio()

equity = portfolio["equity"]

returns = equity.pct_change().fillna(0)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Annual Return",
    f"{annual_return(returns)*100:.2f}%"
)

c2.metric(
    "Volatility",
    f"{annual_volatility(returns)*100:.2f}%"
)

c3.metric(
    "Sharpe",
    f"{sharpe_ratio(returns):.2f}"
)

st.plotly_chart(
    equity_curve(equity),
    width="stretch"
)