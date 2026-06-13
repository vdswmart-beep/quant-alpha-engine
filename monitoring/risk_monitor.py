import pandas as pd


def monitor_drawdown(
    portfolio_returns
):

    equity = (
        1 +
        portfolio_returns
    ).cumprod()

    peak = equity.cummax()

    dd = (
        equity
        /
        peak
        - 1
    )

    return dd.iloc[-1]