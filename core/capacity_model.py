import pandas as pd
import numpy as np


def estimate_capacity(
    volume,
    participation_rate=0.05
):

    daily_capacity = (
        volume.mean()
        * participation_rate
    )

    return daily_capacity