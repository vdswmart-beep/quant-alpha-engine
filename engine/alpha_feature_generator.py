import pandas as pd


class AlphaFeatureGenerator:

    def generate(
        self,
        prices
    ):

        df = pd.DataFrame()

        df["ret_5"] = (
            prices.pct_change(5)
        )

        df["ret_20"] = (
            prices.pct_change(20)
        )

        df["ma_20"] = (
            prices.rolling(20)
            .mean()
        )

        df["ma_50"] = (
            prices.rolling(50)
            .mean()
        )

        df["vol_20"] = (
            prices.pct_change()
            .rolling(20)
            .std()
        )

        return df