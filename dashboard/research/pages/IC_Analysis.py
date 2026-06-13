import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Information Coefficient")

df = pd.read_csv(
    "outputs/ic_results.csv"
)

st.dataframe(df)

fig = px.bar(
    df,
    x="alpha",
    y="score",
    color="ic"
)

st.plotly_chart(
    fig,
    use_container_width=True
)