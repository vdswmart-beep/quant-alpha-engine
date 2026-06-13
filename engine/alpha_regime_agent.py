import pandas as pd


class AlphaRegimeAgent:

    def classify(
        self,
        returns
    ):

        rolling = (
            returns
            .rolling(63)
            .sum()
        )

        regime = pd.Series(
            index=returns.index,
            dtype=str
        )

        regime[
            rolling > 0.05
        ] = "Bull"

        regime[
            rolling < -0.05
        ] = "Bear"

        regime = regime.fillna(
            "Sideways"
        )

        return regime