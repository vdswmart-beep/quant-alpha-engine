import numpy as np
import pandas as pd


def monte_carlo(
    returns,
    n_sims=10000,
    horizon=252,
    initial_capital=100
):
    """
    Monte Carlo simulation.

    Returns
    -------
    simulations_df :
        All terminal portfolio values.

    summary :
        Mean / VaR95 / VaR99.
    """

    mu = returns.mean()
    sigma = returns.std()

    terminal_values = []

    for _ in range(n_sims):

        path = np.random.normal(
            mu,
            sigma,
            horizon
        )

        equity = initial_capital

        for r in path:
            equity *= (1 + r)

        terminal_values.append(
            equity
        )

    simulations_df = pd.DataFrame({
        "terminal_value": terminal_values
    })

    summary = pd.DataFrame({
        "mean": [
            simulations_df["terminal_value"].mean()
        ],
        "var95": [
            simulations_df["terminal_value"].quantile(0.05)
        ],
        "var99": [
            simulations_df["terminal_value"].quantile(0.01)
        ]
    })

    return simulations_df, summary