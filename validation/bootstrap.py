import numpy as np
import pandas as pd


class BootstrapValidator:

    def __init__(
        self,
        returns,
        n_iterations=1000
    ):
        self.returns = pd.Series(
            returns
        ).dropna()

        self.n_iterations = n_iterations

    def run(self):

        sharpes = []

        n = len(self.returns)

        for _ in range(
            self.n_iterations
        ):

            sample = np.random.choice(
                self.returns,
                size=n,
                replace=True
            )

            vol = np.std(sample)

            if vol == 0:
                continue

            sharpe = (
                np.mean(sample)
                / vol
            ) * np.sqrt(252)

            sharpes.append(
                sharpe
            )

        return {
            "mean_sharpe":
                np.mean(sharpes),

            "median_sharpe":
                np.median(sharpes),

            "worst_5pct":
                np.percentile(
                    sharpes,
                    5
                ),

            "best_95pct":
                np.percentile(
                    sharpes,
                    95
                ),
        }