import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Alpha Factory",
    layout="wide"
)

st.title("🏭 Alpha Factory")

# ============================================================
# Load Alpha Ranking
# ============================================================

df = pd.read_csv(
    "outputs/alpha_ranking.csv"
)

# ============================================================
# KPIs
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Generated Alphas",
        len(df)
    )

with col2:
    st.metric(
        "Average Sharpe",
        round(
            df["sharpe"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Average Score",
        round(
            df["score"].mean(),
            2
        )
    )

# ============================================================
# Alpha Table
# ============================================================

st.subheader(
    "Alpha Ranking"
)

st.dataframe(
    df.sort_values(
        "score",
        ascending=False
    ),
    width="stretch"
)

# ============================================================
# Alpha Quality Map
# ============================================================

st.subheader(
    "Alpha Quality Map"
)

plot_df = df.copy()

plot_df["bubble_size"] = (
    plot_df["sortino"]
    .abs()
    .fillna(0)
)

fig = px.scatter(
    plot_df,
    x="sharpe",
    y="score",
    size="bubble_size",
    color="drawdown",
    hover_name="alpha",
    title="Sharpe vs Score"
)

fig.update_traces(
    marker=dict(
        sizemin=5
    )
)

fig.update_layout(
    height=700
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ============================================================
# Top 20 Alphas
# ============================================================

st.subheader(
    "Top 20 Alphas"
)

top20 = (
    df
    .sort_values(
        "score",
        ascending=False
    )
    .head(20)
)

fig = px.bar(
    top20,
    x="alpha",
    y="score",
    color="sharpe",
    title="Top Alpha Scores"
)

st.plotly_chart(
    fig,
    width="stretch"
)