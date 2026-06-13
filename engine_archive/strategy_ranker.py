import pandas as pd


def rank_strategies(results):

    ranking = results.copy()

    ranking["rank_score"] = (

        ranking["sharpe"] * 0.40 +

        ranking["sortino"] * 0.20 +

        ranking["stability"] * 0.20 +

        ranking["hit_ratio"] * 0.20

    )

    return ranking.sort_values(
        "rank_score",
        ascending=False
    )