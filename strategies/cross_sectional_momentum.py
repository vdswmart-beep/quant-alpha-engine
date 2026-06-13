import pandas as pd
import numpy as np


def cross_sectional_momentum(price_dict):

    closes = pd.DataFrame({
        ticker: df["Close"]
        for ticker, df in price_dict.items()
    })

    momentum = closes.pct_change(252)

    ranks = momentum.rank(
        axis=1,
        pct=True
    )

    signals = pd.DataFrame(
        index=ranks.index,
        columns=ranks.columns
    )

    signals[ranks >= 0.8] = 1
    signals[ranks <= 0.2] = -1
    signals = signals.fillna(0)

    return signals