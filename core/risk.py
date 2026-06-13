import pandas as pd
import numpy as np


def correlation_matrix(strategy_returns):

    return strategy_returns.corr()


def inverse_vol_weights(strategy_returns):

    vols = strategy_returns.std()

    inv = 1 / vols

    return inv / inv.sum()


def portfolio_returns(strategy_returns):

    w = inverse_vol_weights(strategy_returns)

    return (strategy_returns * w).sum(axis=1)

def apply_risk_overlay(
    returns,
    max_dd=-0.20
):

    equity = (1 + returns).cumprod()

    peak = equity.cummax()

    dd = equity / peak - 1

    if dd.iloc[-1] < max_dd:

        return returns * 0.5

    return returns