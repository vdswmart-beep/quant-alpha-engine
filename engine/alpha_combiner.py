import random


class AlphaCombiner:

    def combine(
        self,
        alpha_a,
        alpha_b
    ):

        operations = [
            "+",
            "-",
            "*"
        ]

        op = random.choice(
            operations
        )

        return {
            "type": "combined",
            "left": alpha_a,
            "right": alpha_b,
            "operator": op
        }