import pandas as pd
import numpy as np


def allocate_books(book_returns):

    sharpe = (
        book_returns.mean()
        /
        book_returns.std()
    )

    sharpe = sharpe.clip(lower=0)

    weights = (
        sharpe
        /
        sharpe.sum()
    )

    return weights