import pandas as pd


def trend_strategy(
    df,
    fast=50,
    slow=200
):

    data = df.copy()

    data["fast_ma"] = (
        data["Close"]
        .rolling(fast)
        .mean()
    )

    data["slow_ma"] = (
        data["Close"]
        .rolling(slow)
        .mean()
    )

    data["signal"] = 0

    data.loc[
        data["fast_ma"]
        >
        data["slow_ma"],
        "signal"
    ] = 1

    return data