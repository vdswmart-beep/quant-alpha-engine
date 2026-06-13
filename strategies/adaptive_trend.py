import numpy as np


def adaptive_trend(df):

    close = df["Close"]

    vol = close.pct_change().rolling(20).std()

    fast = (
        20 +
        vol.rank(pct=True) * 20
    ).fillna(20)

    slow = (
        100 +
        vol.rank(pct=True) * 50
    ).fillna(100)

    signal = np.zeros(len(df))

    for i in range(120, len(df)):

        f = int(fast.iloc[i])
        s = int(slow.iloc[i])

        ma_fast = (
            close
            .iloc[i-f:i]
            .mean()
        )

        ma_slow = (
            close
            .iloc[i-s:i]
            .mean()
        )

        if ma_fast > ma_slow:
            signal[i] = 1
        else:
            signal[i] = -1

    df["signal"] = signal

    return df