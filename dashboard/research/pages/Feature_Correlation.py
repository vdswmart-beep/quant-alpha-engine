"""
Feature Correlation Dashboard
-----------------------------

Analyse de corrélation entre facteurs / features.

Input:
    outputs/feature_store.csv

Output:
    Heatmap de corrélation
    Top corrélations
    Statistiques générales
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Feature Correlation",
    layout="wide"
)

st.title("Feature Correlation")

PATH = "outputs/feature_store.csv"

try:

    df = pd.read_csv(PATH)

except FileNotFoundError:

    st.error(
        f"File not found: {PATH}"
    )

    st.stop()

# ==========================================================
# Numeric features only
# ==========================================================

numeric_df = df.select_dtypes(
    include=np.number
)

if numeric_df.empty:

    st.warning(
        "No numeric features found."
    )

    st.stop()

# ==========================================================
# Correlation matrix
# ==========================================================

corr = numeric_df.corr()

# ==========================================================
# Summary statistics
# ==========================================================

upper_triangle = corr.where(
    np.triu(
        np.ones(corr.shape),
        k=1
    ).astype(bool)
)

corr_values = (
    upper_triangle
    .stack()
    .abs()
)

avg_corr = corr_values.mean()
max_corr = corr_values.max()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Average Absolute Correlation",
        f"{avg_corr:.3f}"
    )

with col2:

    st.metric(
        "Maximum Absolute Correlation",
        f"{max_corr:.3f}"
    )

# ==========================================================
# Heatmap
# ==========================================================

st.subheader(
    "Correlation Heatmap"
)

fig = px.imshow(

    corr,

    color_continuous_scale="RdBu",

    zmin=-1,

    zmax=1,

    aspect="auto"

)

fig.update_layout(
    height=900
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ==========================================================
# Most correlated pairs
# ==========================================================

st.subheader(
    "Top Correlated Feature Pairs"
)

pairs = []

for i in range(len(corr.columns)):

    for j in range(i + 1, len(corr.columns)):

        pairs.append({

            "feature_1":
            corr.columns[i],

            "feature_2":
            corr.columns[j],

            "correlation":
            corr.iloc[i, j],

            "abs_correlation":
            abs(corr.iloc[i, j])

        })

pairs_df = pd.DataFrame(
    pairs
)

pairs_df = (
    pairs_df
    .sort_values(
        "abs_correlation",
        ascending=False
    )
)

st.dataframe(

    pairs_df[
        [
            "feature_1",
            "feature_2",
            "correlation"
        ]
    ].head(25),

    width="stretch"

)

# ==========================================================
# Download
# ==========================================================

st.download_button(

    label="Download Correlation Matrix",

    data=corr.to_csv().encode(),

    file_name="correlation_matrix.csv",

    mime="text/csv"

)