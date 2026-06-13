import numpy as np
import pandas as pd
from scipy.stats import linregress


class FeatureEngine:

    def __init__(self, df):

        self.df = df.copy()

    def build(self):

        df = self.df

        close = df["Close"]
        returns = close.pct_change()

        # ===================================
        # MOMENTUM
        # ===================================

        horizons = [5, 10, 20, 60, 120, 252]

        for h in horizons:

            df[f"ret_{h}"] = close.pct_change(h)

        # ===================================
        # VOLATILITY
        # ===================================

        for h in [10, 20, 60, 120]:

            df[f"vol_{h}"] = (
                returns
                .rolling(h)
                .std()
                * np.sqrt(252)
            )

        # ===================================
        # SKEW
        # ===================================

        for h in [20, 60]:

            df[f"skew_{h}"] = (
                returns
                .rolling(h)
                .skew()
            )

        # ===================================
        # KURTOSIS
        # ===================================

        for h in [20, 60]:

            df[f"kurt_{h}"] = (
                returns
                .rolling(h)
                .kurt()
            )

        # ===================================
        # TREND QUALITY
        # ===================================

        slopes = []
        r2s = []

        for i in range(len(df)):

            if i < 60:

                slopes.append(np.nan)
                r2s.append(np.nan)
                continue

            y = close.iloc[i-60:i]

            x = np.arange(len(y))

            slope, _, r, _, _ = (
                linregress(x, y)
            )

            slopes.append(slope)

            r2s.append(r**2)

        df["trend_slope"] = slopes

        df["trend_r2"] = r2s

        # ===================================
        # MOVING AVERAGES
        # ===================================

        ma20 = close.rolling(20).mean()
        ma50 = close.rolling(50).mean()
        ma200 = close.rolling(200).mean()

        df["ma20_ma50"] = ma20 / ma50
        df["ma50_ma200"] = ma50 / ma200

        # ===================================
        # Z SCORE
        # ===================================

        mean20 = close.rolling(20).mean()
        std20 = close.rolling(20).std()

        df["zscore_20"] = (
            close - mean20
        ) / std20

        # ===================================
        # DRAWDOWN
        # ===================================

        equity = (
            1 + returns.fillna(0)
        ).cumprod()

        peak = equity.cummax()

        df["drawdown"] = (
            equity / peak - 1
        )

        # ===================================
        # VOLUME FEATURES
        # ===================================

        if "Volume" in df.columns:

            vol_ma = (
                df["Volume"]
                .rolling(20)
                .mean()
            )

            df["volume_shock"] = (
                df["Volume"]
                /
                vol_ma
            )

            df["volume_change"] = (
                df["Volume"]
                .pct_change()
            )

        # ===================================
        # RANGE FEATURES
        # ===================================

        if (
            "High" in df.columns and
            "Low" in df.columns
        ):

            df["daily_range"] = (
                df["High"]
                - df["Low"]
            ) / close

        return df