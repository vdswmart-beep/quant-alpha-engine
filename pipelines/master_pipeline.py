from pipelines.market_pipeline import (
    MarketPipeline
)

from pipelines.alpha_factory_pipeline import (
    AlphaFactoryPipeline
)

from pipelines.research_pipeline import (
    ResearchPipeline
)

from pipelines.validation_pipeline import (
    ValidationPipeline
)

from pipelines.portfolio_pipeline import (
    PortfolioPipeline
)

from pipelines.risk_pipeline import (
    RiskPipeline
)

from pipelines.export_pipeline import (
    ExportPipeline
)


class MasterPipeline:

    def __init__(self):

        self.market = MarketPipeline()

        self.alpha_factory = (
            AlphaFactoryPipeline()
        )

        self.research = (
            ResearchPipeline()
        )

        self.validation = (
            ValidationPipeline()
        )

        self.portfolio = (
            PortfolioPipeline()
        )

        self.risk = (
            RiskPipeline()
        )

        self.export = (
            ExportPipeline()
        )

    def run(self):

        market_data = (
            self.market.run()
        )

        alpha_data = (
            self.alpha_factory.run(
                market_data
            )
        )

        research_results = (
            self.research.run()
        )

        validated = (
            self.validation.run(
                research_results
            )
        )

        portfolio = (
            self.portfolio.run(
                alpha_data[
                    "alpha_universe"
                ],
                alpha_data[
                    "clusters"
                ]
            )
        )

        risk = self.risk.run(
            portfolio["returns"]
        )

        self.export.run(
            alpha_data,
            validated,
            risk
        )

        print(
            "\nMASTER PIPELINE COMPLETE"
        )