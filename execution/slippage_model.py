import numpy as np


def apply_slippage(
    returns,
    bps=2
):

    cost = bps / 10000

    return returns - cost