import pandas as pd
import numpy as np

from engine.ml_ranker import MLRanker


def build_training_set(
    strategy_results
):

    X = strategy_results[
        [
            "sharpe",
            "sortino",
            "calmar",
            "stability",
            "hit_ratio"
        ]
    ]

    y = (
        strategy_results["return"]
        >
        strategy_results["return"].median()
    ).astype(int)

    return X, y


def run_ml_ranking(
    strategy_results
):

    X, y = build_training_set(
        strategy_results
    )

    model = MLRanker()

    model.fit(X, y)

    strategy_results[
        "ml_score"
    ] = model.predict_probability(X)

    return strategy_results.sort_values(
        "ml_score",
        ascending=False
    )