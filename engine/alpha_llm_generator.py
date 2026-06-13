import random

ALPHAS = [

"""
(close / close.shift(5)) - 1
""",

"""
(volume / volume.rolling(20).mean())
""",

"""
(close - close.rolling(20).mean())
/
close.rolling(20).std()
"""
]


class AlphaLLMGenerator:

    def generate(self):

        return random.choice(ALPHAS)

    def generate_batch(
        self,
        n=100
    ):

        return [
            self.generate()
            for _ in range(n)
        ]