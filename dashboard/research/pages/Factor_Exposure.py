import streamlit as st
import pandas as pd

st.title(
    "Factor Exposure"
)

df = pd.read_csv(
    "outputs/factor_exposure.csv"
)

st.dataframe(df)
