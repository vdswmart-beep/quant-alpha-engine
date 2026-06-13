import plotly.graph_objects as go


def equity_curve(equity):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=equity.index,
            y=equity,
            mode="lines",
            name="Portfolio"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig


def drawdown_chart(drawdown):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=drawdown.index,
            y=drawdown,
            fill="tozeroy"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=400
    )

    return fig