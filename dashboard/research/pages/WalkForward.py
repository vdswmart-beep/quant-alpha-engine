import streamlit as st
import plotly.express as px
import sys
import os

# ── FIX: correct import path ────────────────────────────
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
))
from pages.shared.loaders import load_walkforward
# ────────────────────────────────────────────────────────

st.title("🚶 Walk Forward Validation")

df = load_walkforward()

st.dataframe(df)

if len(df.columns) >= 2:
    fig = px.line(
        df,
        x=df.columns[0],
        y=df.columns[1],
        title="Walk Forward Results"
    )
    st.plotly_chart(fig, width="stretch")