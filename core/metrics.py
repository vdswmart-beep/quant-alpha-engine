import numpy as np

TRADING_DAYS = 252


def sharpe(returns):

    vol = returns.std()

    if vol == 0:
        return 0

    return np.sqrt(TRADING_DAYS) * returns.mean() / vol


def sortino(returns):

    downside = returns[returns < 0]

    if len(downside) == 0:
        return 0

    downside_vol = downside.std()

    if downside_vol == 0:
        return 0

    return np.sqrt(TRADING_DAYS) * returns.mean() / downside_vol


def max_drawdown(equity):

    peak = equity.cummax()

    dd = equity / peak - 1

    return dd.min()


def calmar(returns):

    equity = (1 + returns).cumprod()

    mdd = abs(max_drawdown(equity))

    if mdd == 0:
        return 0

    annual_return = (
        equity.iloc[-1]
        ** (252 / len(equity))
        - 1
    )

    return annual_return / mdd


def hit_ratio(returns):

    return (returns > 0).mean()
