import pandas as pd
from datetime import datetime

from engine.alpha_expression_generator import (
    AlphaExpressionGenerator
)

from engine.alpha_expression_engine import (
    AlphaExpressionEngine
)

from engine.alpha_backtester import (
    backtest_alpha
)

from engine.mythos_validator import (
    run_mythos_validation
)

from engine.alpha_evolution import (
    evolve_population
)

from research.memory import (
    save_alpha,
    save_rejected,
    log_research
)


class AlphaResearchLoop:

    def __init__(
        self,
        df,
        n_candidates=100,
        top_n=20
    ):

        self.df = df

        self.n_candidates = n_candidates

        self.top_n = top_n

        self.generator = (
            AlphaExpressionGenerator()
        )

        self.engine = (
            AlphaExpressionEngine()
        )

    def run(self):

        # ── FIX: yfinance MultiIndex (v0.2.x breaking change) ──────────
        if isinstance(self.df.columns, pd.MultiIndex):
            self.df.columns = self.df.columns.get_level_values(0)
        # ────────────────────────────────────────────────────────────────

        close = self.df["Close"]

        returns = (
            close.pct_change()
        )

        candidates = (
            self.generator.generate_batch(
                self.n_candidates
            )
        )

        results = []

        accepted = 0
        rejected = 0

        print(
            f"\nGenerating "
            f"{len(candidates)} alphas..."
        )

        for expression in candidates:

            try:

                signal = (
                    self.engine.evaluate(
                        expression,
                        self.df
                    )
                )

                if signal is None:

                    rejected += 1

                    save_rejected(
                        {
                            "code": expression,
                            "reason": "Expression Error"
                        }
                    )

                    continue

                bt = backtest_alpha(
                    signal,
                    returns
                )

                if bt is None:

                    rejected += 1

                    save_rejected(
                        {
                            "code": expression,
                            "reason": "Backtest Failed"
                        }
                    )

                    continue

                pnl = (
                    signal.shift(1)
                    * returns
                ).dropna()

                mythos = (
                    run_mythos_validation(
                        pnl
                    )
                )

                if mythos is None:

                    rejected += 1

                    save_rejected(
                        {
                            "code": expression,
                            "reason": "Mythos Failed"
                        }
                    )

                    continue

                row = {

                    "expression":
                    expression,

                    "return":
                    float(
                        bt["total_return"]  # FIX: was "return", key is "total_return"
                    ),

                    "sharpe":
                    float(
                        bt["sharpe"]
                    ),

                    "rb_score":
                    float(
                        mythos["rb_score"]
                    ),

                    "dsr":
                    float(
                        mythos["dsr"]
                    ),

                    "pbo":
                    float(
                        mythos["pbo"]
                    ),

                    "stability":
                    float(
                        mythos["stability"]
                    )

                }

                results.append(
                    row
                )

                accepted += 1

            except Exception as e:
            
                print(
                    "\nFAILED:",
                    expression
                )
            
                print(
                    "ERROR:",
                    e
                )
            
                rejected += 1
            
                save_rejected(
                    {
                        "code": expression,
                        "reason": str(e)
                    }
                )

        if len(results) == 0:

            print(
                "\nNo valid alphas found."
            )

            return None

        results_df = pd.DataFrame(
            results
        )

        winners = (

            results_df

            .sort_values(
                "rb_score",
                ascending=False
            )

            .head(
                self.top_n
            )

        )

        print(
            f"\nTop "
            f"{len(winners)} "
            f"survivors selected."
        )

        #
        # Save winners
        #

        for _, row in winners.iterrows():

            save_alpha(
                {
                    "expression":
                    row["expression"],

                    "score":
                    float(
                        row["sharpe"]
                    ),

                    "rb_score":
                    float(
                        row["rb_score"]
                    ),

                    "dsr":
                    float(
                        row["dsr"]
                    ),

                    "pbo":
                    float(
                        row["pbo"]
                    )
                }
            )

        #
        # Evolution
        #

        winner_population = []

        for _, row in winners.iterrows():

            winner_population.append(
                row["expression"]
            )

        children = (
            evolve_population(
                winner_population
            )
        )

        #
        # Research journal
        #

        log_research(

            {

                "date":
                str(
                    datetime.now()
                ),

                "generated":
                len(
                    candidates
                ),

                "accepted":
                accepted,

                "rejected":
                rejected,

                "survivors":
                len(
                    winners
                ),

                "children":
                len(
                    children
                )

            }

        )

        print(
            f"Accepted : {accepted}"
        )

        print(
            f"Rejected : {rejected}"
        )

        print(
            f"Survivors : {len(winners)}"
        )

        print(
            f"Children : {len(children)}"
        )

        return {

            "results":
            results_df,

            "winners":
            winners,

            "children":
            children

        }