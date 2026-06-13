import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "Book Allocation"
)

weights = pd.read_csv(
    "outputs/book_weights.csv"
)

fig = px.pie(
    weights,
    names="book",
    values="weight"
)

st.plotly_chart(
    fig,
    use_container_width=True
)