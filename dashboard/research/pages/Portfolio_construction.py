import streamlit as st
import plotly.express as px

from shared.loaders import (
    load_strategy_results,
    load_rankings
)

st.title("🏗 Portfolio Construction")

rankings = load_rankings()

top_n = st.slider(
    "Number of Strategies",
    5,
    50,
    15
)

selected = rankings.head(top_n)

fig = px.bar(
    selected,
    x="strategy",
    y="score",
    color="score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(selected)