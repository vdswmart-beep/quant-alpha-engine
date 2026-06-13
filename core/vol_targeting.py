import numpy as np


def apply_vol_targeting(
    strategy_returns,
    target_vol=0.15
):

    realized_vol = (
        strategy_returns
        .rolling(20)
        .std()
        * np.sqrt(252)
    )

    leverage = (
        target_vol
        /
        realized_vol
    )

    leverage = leverage.clip(
        lower=0,
        upper=3
    )

    return strategy_returns * leverage.shift(1)