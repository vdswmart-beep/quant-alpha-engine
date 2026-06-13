import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Capacity Analysis",
    layout="wide"
)

st.title("🏦 Strategy Capacity")

df = pd.read_csv(
    "outputs/capacity_report.csv"
)

st.dataframe(
    df,
    use_container_width=True
)

fig = px.bar(
    df,
    y="capacity_usd",
    title="Estimated Capacity (USD)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

if "slippage_bps" in df.columns:

    fig2 = px.bar(
        df,
        y="slippage_bps",
        title="Estimated Slippage (bps)"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )