import pandas as pd
import numpy as np


class SensitivityHeatmap:

    def evaluate(
        self,
        strategy_function,
        parameter_name,
        parameter_values
    ):

        results = []

        for value in parameter_values:

            metrics = strategy_function(value)

            results.append(
                {
                    parameter_name: value,
                    "sharpe": metrics["sharpe"],
                    "return": metrics["return"],
                    "drawdown": metrics["drawdown"]
                }
            )

        return pd.DataFrame(results)