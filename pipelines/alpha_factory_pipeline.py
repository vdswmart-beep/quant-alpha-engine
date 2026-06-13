from engine.alpha_factory_runner import (
    run_alpha_factory
)

from engine.alpha_selector import (
    rank_alpha_universe
)

from core.correlation_filter import (
    remove_correlated_alphas
)

from engine.alpha_cluster import (
    cluster_alphas
)

import pandas as pd


class AlphaFactoryPipeline:

    def run(
        self,
        market_data,
        top_alphas=100
    ):

        alpha_list = []

        for ticker, df in market_data.items():

            alpha_df = run_alpha_factory(df)

            alpha_df.columns = [

                f"{ticker}_{col}"

                for col in alpha_df.columns

            ]

            alpha_list.append(
                alpha_df
            )

        alpha_universe = pd.concat(
            alpha_list,
            axis=1
        )

        ranking = rank_alpha_universe(
            alpha_universe
        )

        selected = (

            ranking["alpha"]

            .head(top_alphas)

            .tolist()

        )

        alpha_universe = (
            alpha_universe[selected]
        )

        alpha_universe = (
            remove_correlated_alphas(
                alpha_universe,
                threshold=0.85
            )
        )

        clusters = cluster_alphas(
            alpha_universe
        )

        return {

            "alpha_universe":
            alpha_universe,

            "ranking":
            ranking,

            "clusters":
            clusters
        }