import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Alpha Galaxy",
    layout="wide"
)

st.title("🌌 Alpha Galaxy")

df = pd.read_csv(
    "outputs/alpha_ranking.csv"
)

features = df[
    [
        "score",
        "sharpe",
        "sortino",
        "drawdown"
    ]
]

scaled = StandardScaler().fit_transform(
    features
)

n_clusters = min(
    5,
    len(df)
)

kmeans = KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(
    scaled
)

fig = go.Figure()

for cluster in sorted(df["cluster"].unique()):

    subset = df[
        df["cluster"] == cluster
    ]

    fig.add_trace(
        go.Scatter3d(
            x=subset["sharpe"],
            y=subset["sortino"],
            z=subset["score"],
            mode="markers+text",
            text=subset["alpha"],
            textposition="top center",
            marker=dict(
                size=8,
                opacity=0.8
            ),
            name=f"Cluster {cluster}"
        )
    )

fig.update_layout(
    height=900,
    scene=dict(
        xaxis_title="Sharpe",
        yaxis_title="Sortino",
        zaxis_title="Score"
    ),
    title="Alpha Galaxy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(
    "Top Ranked Alphas"
)

st.dataframe(
    df.sort_values(
        "score",
        ascending=False
    ),
    use_container_width=True
)