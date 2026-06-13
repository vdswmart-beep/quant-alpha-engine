from engine.alpha_evolution import (
    evolve_population
)

from engine.alpha_memory_writer import (
    save_alpha
)


class EvolutionPipeline:

    def run(
        self,
        winners
    ):

        next_generation = (
            evolve_population(
                winners
            )
        )

        for alpha in next_generation:

            try:

                save_alpha(
                    alpha,
                    score=0,
                    rb_score=0
                )

            except Exception:

                pass

        return next_generation