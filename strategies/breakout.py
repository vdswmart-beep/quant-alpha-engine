import pandas as pd


def breakout_strategy(
    df,
    lookback=50
):

    data = df.copy()

    high = data["High"].rolling(lookback).max()
    low = data["Low"].rolling(lookback).min()

    data["signal"] = 0

    data.loc[data["Close"] > high.shift(1), "signal"] = 1

    data.loc[data["Close"] < low.shift(1), "signal"] = -1

    return data