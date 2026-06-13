import numpy as np


class AlphaEmbeddingEngine:

    def embed(
        self,
        alpha
    ):

        vector = []

        for value in alpha.values():

            vector.append(
                hash(
                    str(value)
                ) % 1000
            )

        return np.array(
            vector,
            dtype=float
        )