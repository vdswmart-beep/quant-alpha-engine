import pandas as pd

from core.metrics import sharpe


def walkforward(returns):

    split = int(len(returns) * 0.7)

    train = returns.iloc[:split]

    test = returns.iloc[split:]

    return {
        "is_sharpe": sharpe(train),
        "oos_sharpe": sharpe(test)
    }
def rolling_walkforward(
    returns,
    train=756,
    test=252
):

    results = []

    start = 0

    while start + train + test < len(returns):

        train_set = returns.iloc[
            start:start+train
        ]

        test_set = returns.iloc[
            start+train:
            start+train+test
        ]

        results.append({
            "is_sharpe":
            sharpe(train_set),

            "oos_sharpe":
            sharpe(test_set)
        })

        start += test

    return results