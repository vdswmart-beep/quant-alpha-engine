import numpy as np
import pandas as pd


def backtest_alpha(
    signal,
    returns
):

    pnl = (
        signal.shift(1)
        * returns
    )

    pnl = pnl.dropna()

    if len(pnl) < 30:

        return None

    sharpe = (
        pnl.mean()
        /
        pnl.std()
    ) * np.sqrt(252)

    equity = (
        1 + pnl
    ).cumprod()

    return {

        "returns": pnl,

        "equity": equity,

        "total_return":
        float(
            equity.iloc[-1] - 1
        ),

        "sharpe":
        float(
            sharpe
        )
    }