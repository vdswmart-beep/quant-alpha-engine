import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Correlation Map",
    layout="wide"
)

st.title("🔗 Alpha Correlation Map")

try:

    corr = pd.read_csv(
        "outputs/correlation_matrix.csv",
        index_col=0
    )

except FileNotFoundError:

    st.error(
        "outputs/correlation_matrix.csv not found. Run run.py first."
    )

    st.stop()

st.metric(
    "Number of Alphas",
    corr.shape[0]
)

fig = px.imshow(
    corr,
    aspect="auto",
    color_continuous_midpoint=0,
    title="Cross-Alpha Correlation Matrix"
)

fig.update_layout(
    height=900
)

st.plotly_chart(
    fig,
    width="stretch"
)

with st.expander(
    "Raw Correlation Matrix"
):

    st.dataframe(
        corr,
        width="stretch"
    )