import pandas as pd


def alpha_summary(
    strategy_results
):

    return pd.DataFrame(
        {
            "mean_return":
            [
                strategy_results[
                    "return"
                ].mean()
            ],

            "mean_sharpe":
            [
                strategy_results[
                    "sharpe"
                ].mean()
            ],

            "best_strategy":
            [
                strategy_results
                .sort_values(
                    "score",
                    ascending=False
                )
                .iloc[0]["strategy"]
            ]
        }
    )