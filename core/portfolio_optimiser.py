import numpy as np
import pandas as pd


def max_sharpe_weights(
    returns_df
):

    sharpe = (
        returns_df.mean()
        /
        returns_df.std()
    )

    sharpe = sharpe.clip(
        lower=0
    )

    weights = (
        sharpe
        /
        sharpe.sum()
    )

    return weights

def optimise_portfolio(
    returns_df
):
    return max_sharpe_weights(
        returns_df
    )

import numpy as np


def sharpe_portfolio(returns):

    vol = returns.std()

    weights = 1 / vol

    weights /= weights.sum()

    portfolio = (
        returns * weights
    ).sum(axis=1)

    return portfolio, weights