import pandas as pd


def build_meta_portfolio(
    book_returns,
    weights
):

    portfolio = (
        book_returns
        * weights
    ).sum(axis=1)

    return portfolio