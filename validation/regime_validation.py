import pandas as pd
import numpy as np


class RegimeValidator:

    def __init__(self):
        pass

    def classify_regime(
        self,
        returns,
        window=63
    ):
        """
        Bull / Bear / Sideways
        """

        rolling_return = (
            returns
            .rolling(window)
            .sum()
        )

        regime = pd.Series(
            index=returns.index,
            dtype="object"
        )

        regime[rolling_return > 0.05] = "Bull"
        regime[rolling_return < -0.05] = "Bear"

        regime = regime.fillna(
            "Sideways"
        )

        return regime

    def validate(
        self,
        strategy_returns
    ):

        regime = self.classify_regime(
            strategy_returns
        )

        results = []

        for r in [
            "Bull",
            "Bear",
            "Sideways"
        ]:

            mask = regime == r

            subset = strategy_returns[
                mask
            ]

            if len(subset) < 30:
                continue

            sharpe = (
                subset.mean()
                /
                subset.std()
            ) * np.sqrt(252)

            results.append({
                "regime": r,
                "sharpe": sharpe,
                "mean_return": subset.mean(),
                "volatility": subset.std()
            })

        return pd.DataFrame(results)