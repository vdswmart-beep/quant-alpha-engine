import pandas as pd


def factor_exposure(
    strategy_returns,
    market_returns,
):

    beta = (
        strategy_returns.cov(
            market_returns
        )
        /
        market_returns.var()
    )

    return beta