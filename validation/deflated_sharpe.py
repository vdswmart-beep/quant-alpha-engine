import numpy as np
from scipy.stats import norm


def deflated_sharpe_ratio(
    sharpe,
    n_obs,
    n_trials
):
    """
    Bailey & Lopez de Prado
    """

    if n_obs <= 1:
        return 0

    sharpe_std = np.sqrt(
        (1 + sharpe ** 2 / 2) / n_obs
    )

    expected_max = norm.ppf(
        1 - 1 / n_trials
    )

    dsr = (
        sharpe - expected_max * sharpe_std
    ) / sharpe_std

    return norm.cdf(dsr)