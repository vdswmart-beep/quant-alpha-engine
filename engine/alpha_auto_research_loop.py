import yfinance as yf
import pandas as pd

from engine.alpha_llm_generator import (
    generate_alpha
)

from engine.alpha_backtester import (
    backtest_alpha
)

from engine.alpha_evaluator import (
    evaluate_alpha
)

from engine.alpha_novelty_engine import (
    is_novel
)

from research.memory import (
    append_memory
)


def run_research_loop():

    print(
        "\nStarting AI Research Loop"
    )

    df = yf.download(
        "SPY",
        start="2010-01-01",
        auto_adjust=True,
        progress=False
    )
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(level=1)

    close = df["Close"]
    volume = df["Volume"]

    returns = close.pct_change()

    for i in range(100):

        alpha_code = (
            generate_alpha()
        )

        if not is_novel(
            alpha_code
        ):
            continue

        local_vars = {

            "close":
            close,

            "volume":
            volume
        }

        try:

            exec(
                alpha_code,
                {},
                local_vars
            )

            signal = (
                local_vars[
                    "signal"
                ]
            )

            metrics = (
                backtest_alpha(
                    signal,
                    returns
                )
            )

            score = (
                evaluate_alpha(
                    metrics
                )
            )

            result = {

                "code":
                alpha_code,

                "score":
                score,

                "metrics":
                metrics
            }

            append_memory(
                "alpha_library.json",
                result
            )

            print(
                f"[{i}] "
                f"Score={score:.2f}"
            )

        except Exception:

            continue