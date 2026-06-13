import numpy as np
import pandas as pd

from validation.bootstrap_validation import (
    bootstrap_sharpe
)

from validation.deflated_sharpe import (
    deflated_sharpe_ratio
)

from validation.pbo import (
    probability_of_backtest_overfitting
)

from validation.regime_validation import (
    RegimeValidator
)

from validation.stress_testing import (
    StressTester
)

from validation.robustness_score import (
    robustness_score
)


def run_mythos_validation(
    returns
):

    returns = pd.Series(
        returns
    ).dropna()

    if len(returns) < 100:

        return None

    sharpe = (
        returns.mean()
        /
        returns.std()
    ) * np.sqrt(252)

    bootstrap = bootstrap_sharpe(
        returns
    )

    dsr = deflated_sharpe_ratio(
        sharpe=sharpe,
        n_obs=len(returns),
        n_trials=100
    )

    pbo = probability_of_backtest_overfitting(
        pd.DataFrame(
            {
                "alpha":
                returns
            }
        )
    )

    regime_validator = (
        RegimeValidator()
    )

    regime_results = (
        regime_validator.validate(
            returns
        )
    )

    if len(regime_results):

        wf_return = (
            regime_results[
                "mean_return"
            ].mean()
        )

    else:

        wf_return = 0

    stress = (
        StressTester()
        .run(returns)
    )

    stability = (
        stress.std()
    )

    stability = 1 / (
        1 + stability
    )

    rb = robustness_score(
        sharpe=sharpe,
        dsr=dsr,
        walkforward_return=wf_return,
        bootstrap_p5=bootstrap["p5"],
        sensitivity_stability=stability
    )

    return {

        "sharpe":
        sharpe,

        "bootstrap_mean":
        bootstrap["mean"],

        "bootstrap_p5":
        bootstrap["p5"],

        "bootstrap_p95":
        bootstrap["p95"],

        "dsr":
        dsr,

        "pbo":
        pbo,

        "rb_score":
        rb,

        "stability":
        stability
    }