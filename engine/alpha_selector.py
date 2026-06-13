import pandas as pd
import numpy as np


def rank_alpha_universe(alpha_returns):

    rows = []

    for alpha in alpha_returns.columns:

        r = alpha_returns[alpha].dropna()

        if len(r) < 252:
            continue

        vol = r.std()

        if vol == 0:
            continue

        sharpe = (
            r.mean()
            / vol
        ) * np.sqrt(252)

        downside = r[r < 0]

        sortino = 0

        if len(downside) > 10:

            sortino = (
                r.mean()
                /
                downside.std()
            ) * np.sqrt(252)

        equity = (1 + r).cumprod()

        peak = equity.cummax()

        drawdown = (
            equity / peak - 1
        ).min()

        score = (
            0.40 * sharpe
            +
            0.30 * sortino
            +
            0.30 * (1 + drawdown)
        )

        rows.append(
            {
                "alpha": alpha,
                "score": score,
                "sharpe": sharpe,
                "sortino": sortino,
                "drawdown": drawdown
            }
        )

    ranking = pd.DataFrame(rows)

    return ranking.sort_values(
        "score",
        ascending=False
    )


def select_top_alphas(
    ranking,
    top_n=100
):

    return ranking.head(top_n)
       