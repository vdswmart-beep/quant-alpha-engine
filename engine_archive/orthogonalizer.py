import numpy as np
from sklearn.decomposition import PCA


def orthogonalize(
    returns
):

    pca = PCA()

    factors = pca.fit_transform(
        returns.fillna(0)
    )

    return factors

