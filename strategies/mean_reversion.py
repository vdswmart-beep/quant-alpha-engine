import pandas as pd


def mean_reversion_strategy(
    df,
    lookback=20
):

    data = df.copy()

    sma = (
        data["Close"]
        .rolling(lookback)
        .mean()
    )

    std = (
        data["Close"]
        .rolling(lookback)
        .std()
    )

    zscore = (
        data["Close"] - sma
    ) / std

    data["signal"] = 0

    data.loc[
        zscore < -1,
        "signal"
    ] = 1

    data.loc[
        zscore > 1,
        "signal"
    ] = -1

    return data
