import pandas as pd
import numpy as np


def volatility_carry_signal(df):

    returns = df["Close"].pct_change()

    vol20 = (
        returns
        .rolling(20)
        .std()
    )

    vol100 = (
        returns
        .rolling(100)
        .std()
    )

    signal = np.where(
        vol20 < vol100,
        1,
        -1
    )

    signal = pd.Series(
        signal,
        index=df.index
    )

    strategy_returns = (
        returns
        * signal.shift(1)
    )

    return strategy_returns.fillna(0)


# Backward compatibility
def vol_carry_strategy(df):

    df = df.copy()

    returns = df["Close"].pct_change()

    vol20 = returns.rolling(20).std()
    vol100 = returns.rolling(100).std()

    df["signal"] = np.where(
        vol20 < vol100,
        1,
        -1
    )

    return df