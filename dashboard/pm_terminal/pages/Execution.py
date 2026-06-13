import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚡ Execution Monitor")

df = pd.read_csv(
    "outputs/execution_log.csv"
)

st.dataframe(df)

if "slippage" in df.columns:

    fig = px.histogram(
        df,
        x="slippage",
        nbins=50
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )