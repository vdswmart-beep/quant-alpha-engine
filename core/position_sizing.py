import numpy as np


def conviction_weight(
    sharpe,
    stability,
    max_weight=0.20
):

    score = (
        sharpe * 0.6
        +
        stability * 0.4
    )

    score = max(
        score,
        0
    )

    return min(
        score / 5,
        max_weight
    )

def volatility_position_size(
    volatility,
    target_vol=0.15,
    max_leverage=3
):

    if volatility <= 0:
        return 1

    leverage = target_vol / volatility

    return min(
        leverage,
        max_leverage
    )