import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def alpha_galaxy(df):

    df = df.copy()

    numeric_cols = [
        "return",
        "sharpe",
        "stability",
        "score"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(
        subset=[
            "return",
            "sharpe",
            "stability"
        ]
    )

    fig = px.scatter_3d(
        df,
        x="sharpe",
        y="stability",
        z="return",
        color="strategy",
        hover_data=["ticker"],
        title="Alpha Galaxy"
    )

    fig.update_traces(
        marker=dict(
            size=8
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=900
    )

    return fig


def correlation_heatmap(corr):

    fig = px.imshow(
        corr,
        aspect="auto",
        text_auto=True,
        color_continuous_scale="RdBu"
    )

    fig.update_layout(
        template="plotly_dark",
        height=800
    )

    return fig


def optimizer_heatmap(df):

    pivot = df.pivot_table(
        values="sharpe",
        index="fast",
        columns="slow"
    )

    fig = px.imshow(
        pivot,
        text_auto=True,
        color_continuous_scale="Viridis"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig