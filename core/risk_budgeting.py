import numpy as np


def risk_budget_weights(
    returns
):

    vol = returns.std()

    inv_vol = 1 / vol

    weights = (
        inv_vol
        /
        inv_vol.sum()
    )

    return weights