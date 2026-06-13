import pandas as pd

from engine.regime_engine import (
    detect_regime
)


def build_regime_history(
    market_data
):

    rows = []

    for ticker, df in market_data.items():

        rows.append(
            {
                "ticker": ticker,
                "regime":
                detect_regime(df)
            }
        )

    return pd.DataFrame(rows)