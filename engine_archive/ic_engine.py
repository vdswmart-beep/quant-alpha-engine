import pandas as pd


def information_coefficient(
    signal,
    future_returns
):

    return signal.corr(
        future_returns
    )