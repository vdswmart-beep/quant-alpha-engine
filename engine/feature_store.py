"""
feature_store.py

Centralized feature engineering module.
Creates all ML / Alpha Factory features.
"""

import numpy as np
import pandas as pd


class FeatureStore:

    @staticmethod
    def build(df: pd.DataFrame) -> pd.DataFrame:

        x = df.copy()

        returns = x["Close"].pct_change()

        x["mom20"] = x["Close"].pct_change(20)
        x["mom60"] = x["Close"].pct_change(60)

        x["vol20"] = returns.rolling(20).std()
        x["vol60"] = returns.rolling(60).std()

        x["ma20"] = x["Close"].rolling(20).mean()
        x["ma50"] = x["Close"].rolling(50).mean()

        x["price_ma20"] = (
            x["Close"] /
            x["ma20"]
        )

        x["price_ma50"] = (
            x["Close"] /
            x["ma50"]
        )

        volume_mean = (
            x["Volume"]
            .rolling(20)
            .mean()
        )

        volume_std = (
            x["Volume"]
            .rolling(20)
            .std()
        )

        x["volume_zscore"] = (
            x["Volume"] - volume_mean
        ) / volume_std

        delta = x["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss

        x["rsi14"] = (
            100 -
            (100 / (1 + rs))
        )

        features = [

            "mom20",
            "mom60",
            "vol20",
            "vol60",
            "price_ma20",
            "price_ma50",
            "volume_zscore",
            "rsi14"

        ]

        return x[features]