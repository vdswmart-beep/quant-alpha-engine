import numpy as np


def annual_return(returns):

    equity = (1 + returns).cumprod()

    years = len(returns) / 252

    return equity.iloc[-1] ** (1 / years) - 1


def annual_volatility(returns):

    return returns.std() * np.sqrt(252)


def sharpe_ratio(returns):

    vol = annual_volatility(returns)

    if vol == 0:
        return 0

    return annual_return(returns) / vol


def max_drawdown(equity):

    peak = equity.cummax()

    dd = equity / peak - 1

    return dd.min()


def calmar_ratio(returns):

    equity = (1 + returns).cumprod()

    mdd = abs(max_drawdown(equity))

    if mdd == 0:
        return 0

    return annual_return(returns) / mdd