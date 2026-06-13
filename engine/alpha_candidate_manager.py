from engine.alpha_expression_generator import (
    generate_expression
)

from engine.alpha_novelty_engine import (
    is_novel
)


def create_candidates(
    n=100
):

    candidates = []

    attempts = 0

    while (
        len(candidates) < n
        and attempts < n * 10
    ):

        alpha = generate_expression()

        if is_novel(alpha):

            candidates.append(
                alpha
            )

        attempts += 1

    return candidates