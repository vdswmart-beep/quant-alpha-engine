import pandas as pd
import numpy as np


def pairs_trading_signal(
    asset_a,
    asset_b,
    lookback=20,
):

    spread = (
        asset_a["Close"]
        - asset_b["Close"]
    )

    zscore = (
        spread
        - spread.rolling(
            lookback
        ).mean()
    ) / (
        spread.rolling(
            lookback
        ).std()
    )

    signal = pd.Series(
        0,
        index=spread.index
    )

    signal[zscore > 2] = -1

    signal[zscore < -2] = 1

    returns = (
        spread.pct_change()
        * signal.shift(1)
    )

    return returns.fillna(0)