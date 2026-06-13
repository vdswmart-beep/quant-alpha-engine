import streamlit as st
import plotly.express as px
import sys
import os

# ── FIX: correct import path ────────────────────────────
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
))
from pages.shared.loaders import load_optimizer
# ────────────────────────────────────────────────────────

st.title("⚙ Strategy Optimizer")

df = load_optimizer()

st.dataframe(df)

if "sharpe" in df.columns:
    fig = px.bar(
        df.sort_values("sharpe", ascending=False).head(20),
        x=df.columns[0],
        y="sharpe",
        title="Top Parameter Sets by Sharpe"
    )
    st.plotly_chart(fig, width="stretch")

st.subheader("Top Parameter Sets")
best = df.sort_values(
    "sharpe", ascending=False
).head(20) if "sharpe" in df.columns else df.head(20)
st.dataframe(best)