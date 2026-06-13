import random


def crossover(
    expr_a,
    expr_b
):
    """
    Expression crossover.

    Exemple :

    rank(close,20)

    +

    zscore(volume,50)

    devient :

    (rank(close,20))+(zscore(volume,50))
    """

    operator = random.choice(
        [
            "+",
            "-",
            "*"
        ]
    )

    return (
        f"({expr_a})"
        f"{operator}"
        f"({expr_b})"
    )