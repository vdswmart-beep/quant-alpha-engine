import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regime History")

df = pd.read_csv(
    "outputs/regime_history.csv"
)

st.dataframe(df)

if "regime" in df.columns:

    counts = (
        df["regime"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "regime",
        "count"
    ]

    fig = px.pie(
        counts,
        names="regime",
        values="count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )