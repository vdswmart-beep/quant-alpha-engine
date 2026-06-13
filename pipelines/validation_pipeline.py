from validation.alpha_survivor import (
    alpha_survivor_filter
)


class ValidationPipeline:

    def run(
        self,
        research_results
    ):

        if research_results.empty:

            return research_results

        survivors = (
            alpha_survivor_filter(
                research_results
            )
        )

        return survivors