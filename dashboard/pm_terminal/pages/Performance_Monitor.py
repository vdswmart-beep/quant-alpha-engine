import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Performance Monitor")

df = pd.read_csv(
    "outputs/performance_monitor.csv"
)

st.dataframe(df)

for col in df.columns:

    if col.lower() != "date":

        fig = px.line(
            df,
            y=col,
            title=col
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )