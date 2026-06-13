import pandas as pd


def build_alpha_books(
    alpha_returns,
    clusters
):

    books = {}

    for cluster in sorted(
        clusters["cluster"].unique()
    ):

        members = clusters.loc[
            clusters["cluster"] == cluster,
            "alpha"
        ].tolist()

        members = [
            m
            for m in members
            if m in alpha_returns.columns
        ]

        if len(members) == 0:
            continue

        books[
            f"Book_{cluster}"
        ] = (
            alpha_returns[members]
            .mean(axis=1)
        )

    return pd.DataFrame(books)