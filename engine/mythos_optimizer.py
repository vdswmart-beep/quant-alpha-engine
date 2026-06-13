from validation.bootstrap_validation import (
    bootstrap_validation
)

from validation.deflated_sharpe import (
    deflated_sharpe_ratio
)

from validation.regime_validation import (
    regime_validation
)

from validation.pbo import pbo_score

from validation.robustness_score import (
    robustness_score
)


def mythos_score(
    returns
):

    bs = bootstrap_validation(
        returns
    )

    dsr = deflated_sharpe_ratio(
        returns
    )

    regime = regime_validation(
        returns
    )

    pbo = pbo_score(
        returns
    )

    rb = robustness_score(
        bs,
        dsr,
        regime,
        pbo
    )

    return {

        "bootstrap": bs,

        "deflated_sharpe": dsr,

        "regime_score": regime,

        "pbo": pbo,

        "rb_score": rb
    }