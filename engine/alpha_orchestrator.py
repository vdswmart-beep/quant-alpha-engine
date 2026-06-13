import pandas as pd

from engine.alpha_research_agent import (
    AlphaResearchAgent
)

from engine.alpha_evaluator import (
    AlphaEvaluator
)

from engine.alpha_tournament import (
    AlphaTournament
)

from engine.mythos_optimizer import (
    MythosOptimizer
)


class AlphaOrchestrator:

    def __init__(self):

        self.agent = (
            AlphaResearchAgent()
        )

        self.evaluator = (
            AlphaEvaluator()
        )

        self.tournament = (
            AlphaTournament()
        )

        self.optimizer = (
            MythosOptimizer()
        )

    def run(
        self,
        returns
    ):

        ideas = (
            self.agent.generate_ideas(
                100
            )
        )

        results = []

        for alpha in ideas:

            metrics = (
                self.evaluator.evaluate(
                    returns
                )
            )

            row = alpha.copy()

            row.update(metrics)

            results.append(row)

        df = pd.DataFrame(
            results
        )

        winners = (
            self.tournament.run(df)
        )

        winners = (
            self.optimizer.optimize(
                winners
            )
        )

        return winners