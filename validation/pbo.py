import numpy as np
import pandas as pd


def probability_of_backtest_overfitting(
    returns_matrix,
    n_splits=10
):
    """
    Simplified PBO

    returns_matrix :
    rows = dates
    cols = strategies
    """

    returns_matrix = returns_matrix.copy()

    n = len(returns_matrix)

    split_size = n // n_splits

    failures = 0
    tests = 0

    for i in range(n_splits):

        start = i * split_size
        end = start + split_size

        test = returns_matrix.iloc[start:end]

        train = pd.concat(
            [
                returns_matrix.iloc[:start],
                returns_matrix.iloc[end:]
            ]
        )

        train_sharpes = (
            train.mean()
            / train.std()
        )

        best_strategy = (
            train_sharpes.idxmax()
        )

        test_sharpe = (
            test[best_strategy].mean()
            /
            test[best_strategy].std()
        )

        median_test = (
            test.mean()
            /
            test.std()
        ).median()

        if test_sharpe < median_test:
            failures += 1

        tests += 1

    return failures / tests
