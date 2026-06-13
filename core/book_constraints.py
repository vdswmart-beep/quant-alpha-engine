import numpy as np


def apply_book_constraints(
    weights,
    max_weight=0.20
):

    weights = weights.clip(
        upper=max_weight
    )

    return weights / weights.sum()
