import pandas as pd


def rank_features(feature_df):

    cols = [

        c

        for c in feature_df.columns

        if c != "ticker"

    ]

    ranking = []

    for col in cols:

        ranking.append(

            {

                "feature": col,

                "mean": feature_df[col].mean(),

                "std": feature_df[col].std()

            }

        )

    return pd.DataFrame(
        ranking
    )