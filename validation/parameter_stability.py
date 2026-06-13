import pandas as pd
import numpy as np


class ParameterStability:

    def evaluate(
        self,
        parameter_values,
        sharpe_values
    ):

        sharpe_values = np.array(
            sharpe_values
        )

        smoothness = (
            1
            /
            (
                1
                +
                np.std(
                    np.diff(
                        sharpe_values
                    )
                )
            )
        )

        robustness = (
            np.mean(
                sharpe_values > 0
            )
        )

        return {
            "smoothness": smoothness,
            "robustness": robustness,
            "stability_score":
                (
                    smoothness
                    +
                    robustness
                ) / 2
        }