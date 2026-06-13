import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚦 Crowding Analysis")

df = pd.read_csv(
    "outputs/crowding_scores.csv"
)

st.dataframe(df)

x_col = "alpha" if "alpha" in df.columns else df.columns[0]
y_col = "crowding_score" if "crowding_score" in df.columns else df.columns[1]

fig = px.bar(
    df,
    x=x_col,
    y=y_col,
    title="Crowding Scores"
)

st.plotly_chart(
    fig,
    width="stretch"
)