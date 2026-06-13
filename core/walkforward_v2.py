import numpy as np


def rolling_walkforward(
    returns,
    train_size=252 * 3,
    test_size=252
):

    results = []

    start = 0

    while (
        start
        + train_size
        + test_size
        < len(returns)
    ):

        train = returns.iloc[
            start :
            start + train_size
        ]

        test = returns.iloc[
            start + train_size :
            start + train_size + test_size
        ]

        is_sharpe = (
            train.mean()
            /
            (train.std() + 1e-6)
        ) * np.sqrt(252)

        oos_sharpe = (
            test.mean()
            /
            (test.std() + 1e-6)
        ) * np.sqrt(252)

        results.append(
            {
                "is_sharpe": is_sharpe,
                "oos_sharpe": oos_sharpe,
            }
        )

        start += test_size

    return results


def stability_score(
    rolling_results
):

    if len(rolling_results) == 0:
        return 0

    sharpes = [
        x["oos_sharpe"]
        for x in rolling_results
    ]

    return np.mean(sharpes) / (
        np.std(sharpes) + 1e-6
    )