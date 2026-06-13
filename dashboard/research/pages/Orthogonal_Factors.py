import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Orthogonal Factors")

df = pd.read_csv(
    "outputs/orthogonal_factors.csv"
)

st.dataframe(df.head())

for col in df.columns:

    fig = px.line(
        df,
        y=col,
        title=col
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )