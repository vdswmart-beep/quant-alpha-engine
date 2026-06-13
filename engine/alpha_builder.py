import numpy as np


def build_alpha(df, config):

    close = df["Close"]

    if config["type"] == "momentum":

        lb = config["lookback"]

        signal = np.sign(

            close.pct_change(lb)

        )

        return signal

    if config["type"] == "mean_reversion":

        lb = config["lookback"]

        mean = close.rolling(lb).mean()

        signal = -np.sign(

            close - mean

        )

        return signal

    if config["type"] == "breakout":

        lb = config["lookback"]

        high = close.rolling(lb).max()

        low = close.rolling(lb).min()

        signal = np.where(

            close > high.shift(1),
            1,

            np.where(
                close < low.shift(1),
                -1,
                0
            )
        )

        return signal

    return np.zeros(len(df))