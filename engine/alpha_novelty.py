import numpy as np


class AlphaNovelty:

    def score(
        self,
        alpha,
        previous_alphas
    ):

        if len(
            previous_alphas
        ) == 0:

            return 1.0

        matches = 0

        for old in previous_alphas:

            similarity = 0

            for k in alpha:

                if (
                    k in old
                    and alpha[k]
                    == old[k]
                ):
                    similarity += 1

            similarity /= max(
                len(alpha),
                1
            )

            matches += similarity

        average_similarity = (
            matches
            /
            len(previous_alphas)
        )

        novelty = (
            1
            -
            average_similarity
        )

        return float(
            np.clip(
                novelty,
                0,
                1
            )
        )