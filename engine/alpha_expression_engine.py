import numpy as np
import pandas as pd


class AlphaExpressionEngine:

    def __init__(self):
        pass

    # =========================
    # OPERATORS
    # =========================

    @staticmethod
    def rank(series, window):
        return series.rolling(window).rank(pct=True)

    @staticmethod
    def zscore(series, window):
        mean = series.rolling(window).mean()
        std = series.rolling(window).std()
        return (series - mean) / std

    @staticmethod
    def delta(series, window):
        return series.diff(window)

    @staticmethod
    def ts_mean(series, window):
        return series.rolling(window).mean()

    @staticmethod
    def ts_std(series, window):
        return series.rolling(window).std()

    # =========================
    # EVALUATION
    # =========================

    def evaluate(self, expression, df):

        # ── FIX: yfinance MultiIndex (v0.2.x breaking change) ──────────
        if isinstance(df.columns, pd.MultiIndex):
            df = df.copy()
            df.columns = df.columns.get_level_values(0)
        # ────────────────────────────────────────────────────────────────

        close = df["Close"]
        volume = df["Volume"]

        returns = close.pct_change()
        volatility = returns.rolling(20).std()

        context = {
            "close": close,
            "volume": volume,
            "returns": returns,
            "volatility": volatility,
            "rank": self.rank,
            "zscore": self.zscore,
            "delta": self.delta,
            "ts_mean": self.ts_mean,
            "ts_std": self.ts_std
        }

        try:
            signal = eval(expression, {"__builtins__": {}}, context)

            # ── FIX: eval may return DataFrame if columns weren't flattened ──
            if isinstance(signal, pd.DataFrame):
                signal = signal.squeeze()
            # ────────────────────────────────────────────────────────────────

            signal = (
                signal
                .replace([np.inf, -np.inf], np.nan)
                .fillna(0)
            )

            if not isinstance(signal, pd.Series):
                signal = pd.Series(signal, index=df.index)

            return signal

        except Exception as e:
            print(f"Expression Error: {expression}")
            print(e)
            return None