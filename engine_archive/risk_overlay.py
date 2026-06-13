import pandas as pd


def apply_risk_overlay(
    returns,
    max_daily_loss=-0.03
):

    r = returns.copy()

    r[r < max_daily_loss] = (
        max_daily_loss
    )

    return r