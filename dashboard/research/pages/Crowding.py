import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚦 Crowding Analysis")

df = pd.read_csv(
    "outputs/crowding_scores.csv"
)

st.dataframe(df)

fig = px.bar(
    df,
    x="strategy",
    y="crowding_score",
    title="Crowding Scores"
)

st.plotly_chart(
    fig,
    use_container_width=True
)