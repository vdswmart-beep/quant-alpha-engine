import pandas as pd


def robustness_score(row):

    return (
        0.30 * row["sharpe"]
        + 0.25 * row["sortino"]
        + 0.20 * row["stability"]
        + 0.15 * row["calmar"]
        + 0.10 * row["hit_ratio"]
    )


def build_alpha_universe(df):

    df["score"] = df.apply(
        robustness_score,
        axis=1
    )

    return df