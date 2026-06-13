import random


FEATURES = [

    "close",
    "returns",
    "volume",
    "volatility"

]


OPERATORS = [

    "rank",
    "zscore",
    "delta",
    "ts_mean",
    "ts_std"

]


WINDOWS = [

    5,
    10,
    20,
    50,
    100,
    200

]


COMBINATIONS = [

    "single",
    "double"

]


class AlphaExpressionGenerator:

    def __init__(self):

        pass

    def generate_single(self):

        feature = random.choice(
            FEATURES
        )

        operator = random.choice(
            OPERATORS
        )

        window = random.choice(
            WINDOWS
        )

        return (
            f"{operator}"
            f"({feature},{window})"
        )

    def generate_double(self):

        expr1 = self.generate_single()

        expr2 = self.generate_single()

        operation = random.choice(
            [
                "+",
                "-",
                "*"
            ]
        )

        return (
            f"({expr1})"
            f"{operation}"
            f"({expr2})"
        )

    def generate(self):

        mode = random.choice(
            COMBINATIONS
        )

        if mode == "single":

            return (
                self.generate_single()
            )

        return (
            self.generate_double()
        )

    def generate_batch(
        self,
        n=100
    ):

        return [

            self.generate()

            for _ in range(n)

        ]