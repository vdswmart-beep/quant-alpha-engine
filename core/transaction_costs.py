import pandas as pd
import numpy as np


def apply_transaction_costs(
    returns,
    signal,
    cost_bps=5
):

    turnover = signal.diff().abs()

    costs = turnover * (
        cost_bps / 10000
    )

    return returns - costs.fillna(0)