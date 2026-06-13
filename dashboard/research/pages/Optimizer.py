import streamlit as st

from dashboard.research.pages.shared.loaders import load_optimizer
from shared.graphs import optimizer_heatmap

st.title("⚙ Strategy Optimizer")

df = load_optimizer()

st.plotly_chart(
    optimizer_heatmap(df),
    use_container_width=True
)

best = df.sort_values(
    "sharpe",
    ascending=False
).head(20)

st.subheader("Top Parameter Sets")

st.dataframe(best)