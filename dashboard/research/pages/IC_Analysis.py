import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Information Coefficient")

df = pd.read_csv(
    "outputs/ic_results.csv"
)

st.dataframe(df)

x_col = "alpha" if "alpha" in df.columns else df.columns[0]
y_col = "ic" if "ic" in df.columns else df.columns[1]

fig = px.bar(
    df,
    x=x_col,
    y=y_col,
    title="Information Coefficient by Alpha"
)

st.plotly_chart(
    fig,
    width="stretch"
)