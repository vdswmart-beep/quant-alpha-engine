import streamlit as st
import plotly.express as px

from shared.loaders import load_walkforward

st.title("🚶 Walk Forward Validation")

df = load_walkforward()

fig = px.scatter(
    df,
    x="is_sharpe",
    y="oos_sharpe",
    color="strategy",
    hover_name="strategy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

df["degradation"] = (
    df["oos_sharpe"]
    /
    df["is_sharpe"]
)

st.dataframe(df)