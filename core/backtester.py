import pandas as pd

from core.metrics import (
    sharpe,
    sortino,
    calmar,
    hit_ratio,
    max_drawdown
)


def backtest(df):

    if "signal" not in df.columns:
        raise ValueError(
            "Strategy dataframe must contain signal column"
        )

    data = df.copy()

    data["returns"] = (
        data["Close"]
        .pct_change()
        .fillna(0)
    )

    # no lookahead bias

    data["strategy_return"] = (
        data["signal"]
        .shift(1)
        .fillna(0)
        * data["returns"]
    )

    equity = (
        1 + data["strategy_return"]
    ).cumprod()

    metrics = {
        "returns": data["strategy_return"],
        "equity": equity,
        "sharpe": sharpe(
            data["strategy_return"]
        ),
        "sortino": sortino(
            data["strategy_return"]
        ),
        "calmar": calmar(
            data["strategy_return"]
        ),
        "hit_ratio": hit_ratio(
            data["strategy_return"]
        ),
        "drawdown": max_drawdown(
            equity
        )
    }

    return metrics