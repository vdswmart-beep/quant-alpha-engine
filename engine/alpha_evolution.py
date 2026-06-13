from engine.alpha_mutator import (
    mutate_alpha
)

from engine.alpha_crossover import (
    crossover
)


def evolve_population(
    winners
):

    population = []

    #
    # winners =
    # list of expressions
    #

    for expr in winners:

        try:

            child = mutate_alpha(
                expr
            )

            population.append(
                child
            )

        except Exception:

            pass

    #
    # crossover
    #

    for i in range(
        len(winners) - 1
    ):

        try:

            child = crossover(

                winners[i],

                winners[i + 1]

            )

            population.append(
                child
            )

        except Exception:

            pass

    return population