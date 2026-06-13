import pandas as pd

from core.backtester import backtest
from core.metrics import sharpe


def optimize(data, strategy_func):

    results = []

    for fast in [10,20,50,100]:
        for slow in [50,100,150,200]:

            if fast >= slow:
                continue

            result = strategy_func(
                data.copy(),
                fast=fast,
                slow=slow
            )

            bt = backtest(result)

            results.append(
                {
                    "fast": fast,
                    "slow": slow,
                    "sharpe": bt["sharpe"]
                }
            )

    return pd.DataFrame(results)