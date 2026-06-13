import numpy as np


def rolling_sharpe(
    returns,
    window=60
):

    return (

        returns
        .rolling(window)
        .mean()

        /

        returns
        .rolling(window)
        .std()

    ) * np.sqrt(252)