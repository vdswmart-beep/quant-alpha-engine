import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def factor_exposure(strategy_returns, factor_returns):

    aligned = pd.concat(
        [strategy_returns, factor_returns],
        axis=1
    ).dropna()

    y = aligned.iloc[:, 0].values

    X = aligned.iloc[:, 1:].values

    model = LinearRegression()

    model.fit(X, y)

    return pd.Series(
        model.coef_,
        index=factor_returns.columns,
        name="beta"
    )