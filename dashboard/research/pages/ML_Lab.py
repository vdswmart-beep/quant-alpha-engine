import streamlit as st
import pandas as pd

st.title(
    "ML Ranking Engine"
)

importance = pd.read_csv(
    "outputs/feature_importance.csv"
)

st.dataframe(
    importance
)

st.bar_chart(
    importance.set_index(
        "feature"
    )["importance"]
)