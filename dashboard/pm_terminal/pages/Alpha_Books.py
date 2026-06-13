import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📚 Alpha Books")

df = pd.read_csv(
    "outputs/alpha_books.csv"
)

st.dataframe(df)

fig = px.line(
    df,
    title="Alpha Books Performance"
)

st.plotly_chart(
    fig,
    width="stretch"
)