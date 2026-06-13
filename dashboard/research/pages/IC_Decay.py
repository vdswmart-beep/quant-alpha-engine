import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⏳ IC Decay")

df = pd.read_csv(
    "outputs/ic_decay.csv"
)

st.dataframe(df)

fig = px.line(
    df,
    x="lag",
    y="ic",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)