import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔗 Alpha Clusters")

df = pd.read_csv(
    "outputs/alpha_clusters.csv"
)

st.dataframe(df)

fig = px.scatter(
    df,
    x="alpha",
    y="cluster",
    color="cluster"
)

st.plotly_chart(
    fig,
    use_container_width=True
)