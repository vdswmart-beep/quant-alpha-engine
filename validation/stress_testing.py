import pandas as pd
import numpy as np


class StressTester:

    def run(
        self,
        returns
    ):

        scenarios = {}

        scenarios["normal"] = (
            returns.mean()
        )

        scenarios["half_returns"] = (
            returns * 0.5
        ).mean()

        scenarios["double_returns"] = (
            returns * 2
        ).mean()

        scenarios["volatility_shock"] = (
            returns +
            np.random.normal(
                0,
                returns.std(),
                len(returns)
            )
        ).mean()

        scenarios["crash"] = (
            returns - 0.02
        ).mean()

        return pd.Series(
            scenarios
        )