import numpy as np
import pandas as pd

def inverse_vol_portfolio(returns_df):

    vol = returns_df.std().replace(0, np.nan)

    weights = 1 / vol
    weights = weights.replace([np.inf, -np.inf], np.nan)

    weights = weights / weights.sum()

    weights = weights.fillna(0)

    portfolio_returns = (returns_df * weights).sum(axis=1)

    return portfolio_returns, weights