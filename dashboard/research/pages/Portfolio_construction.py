import streamlit as st
import plotly.express as px
import sys
import os

# ── FIX: correct import path ────────────────────────────
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
))
from pages.shared.loaders import load_strategy_results, load_rankings
# ────────────────────────────────────────────────────────

st.title("🏗 Portfolio Construction")

df = load_strategy_results()
st.subheader("Strategy Results")
st.dataframe(df)

rankings = load_rankings()
st.subheader("Alpha Rankings")
st.dataframe(rankings)

if len(rankings.columns) >= 2:
    fig = px.bar(
        rankings.head(20),
        x=rankings.columns[0],
        y=rankings.columns[1],
        title="Top 20 Alphas by Rank"
    )
    st.plotly_chart(fig, width="stretch")