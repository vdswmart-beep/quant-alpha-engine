import pandas as pd


class AlphaMicrostructureAgent:

    def analyze(
        self,
        volume,
        spread
    ):

        liquidity_score = (

            volume.mean()

            /

            (
                spread.mean()
                + 1e-6
            )

        )

        return {
            "liquidity_score":
                liquidity_score
        }