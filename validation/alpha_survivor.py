import pandas as pd


def alpha_survivor_filter(
    df,
    min_sharpe=1.2,
    min_dsr=0.70,
    min_rb=70,
    max_pbo=0.20
):
    """
    Keeps only robust alphas
    """

    survivors = df[
        (df["sharpe"] >= min_sharpe)
        &
        (df["dsr"] >= min_dsr)
        &
        (df["rb_score"] >= min_rb)
        &
        (df["pbo"] <= max_pbo)
    ]

    return survivors.sort_values(
        "rb_score",
        ascending=False
    )