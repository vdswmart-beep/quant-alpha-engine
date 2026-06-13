import pandas as pd


class AlphaEngine:

    def score(
        self,
        sharpe,
        sortino,
        calmar,
        stability,
        hit_ratio
    ):

        return (
            0.30 * sharpe
            + 0.25 * sortino
            + 0.20 * calmar
            + 0.15 * stability
            + 0.10 * hit_ratio
        )