import pandas as pd

from core.hrp import hrp_weights


def build_meta_portfolio(
    books
):

    if books.shape[1] < 2:

        weights = pd.Series(
            [1.0],
            index=books.columns
        )

    else:

        weights = hrp_weights(
            books
        )

    portfolio = (
        books * weights
    ).sum(axis=1)

    return portfolio, weights