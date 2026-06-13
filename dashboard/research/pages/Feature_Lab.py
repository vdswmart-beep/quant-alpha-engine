import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "Feature Laboratory"
)

df = pd.read_csv(
    "outputs/feature_store.csv"
)

st.dataframe(df)

feature = st.selectbox(
    "Feature",
    [
        c
        for c in df.columns
        if c != "ticker"
    ]
)

fig = px.bar(

    df,

    x="ticker",

    y=feature

)

st.plotly_chart(
    fig,
    use_container_width=True
)

feature_stats = pd.DataFrame({
    "feature": df.columns,
    "mean_abs": df.abs().mean()
})

fig = px.bar(
    feature_stats,
    x="feature",
    y="mean_abs"
)