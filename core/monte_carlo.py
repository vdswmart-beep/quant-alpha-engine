import numpy as np


def monte_carlo_risk(
    returns,
    n_sims=10000,
    horizon=252
):

    mu = returns.mean()

    sigma = returns.std()

    outcomes = []

    for _ in range(n_sims):

        path = np.random.normal(
            mu,
            sigma,
            horizon
        )

        wealth = (
            np.prod(
                1 + path
            )
        )

        outcomes.append(
            wealth
        )

    outcomes = np.array(
        outcomes
    )

    return {

        "mean":
            outcomes.mean(),

        "p5":
            np.percentile(
                outcomes,
                5
            ),

        "p1":
            np.percentile(
                outcomes,
                1
            ),

        "best":
            outcomes.max(),

        "worst":
            outcomes.min()
    }