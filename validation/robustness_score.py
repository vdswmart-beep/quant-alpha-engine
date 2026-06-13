import numpy as np


def robustness_score(
    sharpe,
    dsr,
    walkforward_return,
    bootstrap_p5,
    sensitivity_stability
):
    """
    Score 0 -> 100
    """

    sharpe_score = min(
        sharpe / 3,
        1
    )

    wf_score = max(
        walkforward_return,
        0
    )

    bootstrap_score = min(
        bootstrap_p5 / 2,
        1
    )

    stability_score = min(
        sensitivity_stability,
        1
    )

    rb = (
        sharpe_score * 0.25
        + dsr * 0.25
        + wf_score * 0.20
        + bootstrap_score * 0.15
        + stability_score * 0.15
    )

    return round(
        rb * 100,
        2
    )