import pandas as pd


def crowding_score(

    strategy_returns

):

    corr = (
        strategy_returns
        .corr()
        .abs()
    )

    score = corr.mean()

    return score