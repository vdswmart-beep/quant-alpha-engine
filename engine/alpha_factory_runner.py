import pandas as pd
import numpy as np

from engine.alpha_factory import AlphaFactory
from engine.alpha_builder import build_alpha


def run_alpha_factory(df):

    factory = AlphaFactory()

    alpha_configs = factory.generate()

    alpha_returns = {}

    returns = df["Close"].pct_change()

    for i, config in enumerate(alpha_configs):

        try:

            signal = build_alpha(
                df,
                config
            )

            signal = pd.Series(
                signal,
                index=df.index
            )

            alpha_ret = (
                returns
                * signal.shift(1)
            )

            alpha_name = (
                f"Alpha_{i}"
            )

            alpha_returns[
                alpha_name
            ] = alpha_ret

        except Exception:

            continue

    alpha_df = pd.DataFrame(
        alpha_returns
    )

    return alpha_df