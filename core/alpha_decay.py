import pandas as pd
import numpy as np


def alpha_decay(signal, returns):

    future = returns.shift(-1)

    rolling_ic = (
        signal
        .rolling(60)
        .corr(future)
    )

    return rolling_ic