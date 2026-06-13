import numpy as np


class AlphaSurvival:

    def probability(
        self,
        bootstrap_sharpes
    ):

        bootstrap_sharpes = np.array(
            bootstrap_sharpes
        )

        survival = (
            bootstrap_sharpes > 0
        ).mean()

        return {
            "survival_probability":
            float(survival)
        }