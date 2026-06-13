from core.vol_targeting import (
    apply_vol_targeting
)

from core.monte_carlo_v2 import (
    monte_carlo
)


class RiskPipeline:

    def run(
        self,
        portfolio_returns
    ):

        portfolio_returns = (

            apply_vol_targeting(
                portfolio_returns,
                target_vol=0.12
            )

        )

        mc_paths, mc_summary = (

            monte_carlo(
                portfolio_returns
            )

        )

        return {

            "returns":
            portfolio_returns,

            "mc_paths":
            mc_paths,

            "mc_summary":
            mc_summary
        }