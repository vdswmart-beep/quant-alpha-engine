import numpy as np
import pandas as pd

from scipy.cluster.hierarchy import (
    linkage,
    dendrogram
)

from scipy.spatial.distance import squareform


# ==========================================================
# DISTANCE MATRIX
# ==========================================================

def correlation_distance(corr):

    return np.sqrt(
        (1 - corr) / 2
    )


# ==========================================================
# QUASI DIAGONALIZATION
# ==========================================================

def get_quasi_diag(link):

    link = link.astype(int)

    sort_ix = pd.Series(
        [link[-1, 0], link[-1, 1]]
    )

    num_items = link[-1, 3]

    while sort_ix.max() >= num_items:

        sort_ix.index = range(
            0,
            sort_ix.shape[0] * 2,
            2
        )

        df0 = sort_ix[
            sort_ix >= num_items
        ]

        i = df0.index

        j = df0.values - num_items

        sort_ix.loc[i] = link[j, 0]

        df1 = pd.Series(
            link[j, 1],
            index=i + 1
        )

        sort_ix = pd.concat(
            [sort_ix, df1]
        )

        sort_ix = sort_ix.sort_index()

        sort_ix.index = range(
            sort_ix.shape[0]
        )

    return sort_ix.tolist()


# ==========================================================
# CLUSTER VARIANCE
# ==========================================================

def cluster_variance(
    cov,
    cluster_items
):

    cov_slice = cov.loc[
        cluster_items,
        cluster_items
    ]

    weights = (
        1 /
        np.diag(cov_slice)
    )

    weights /= weights.sum()

    variance = (
        weights
        @ cov_slice
        @ weights
    )

    return variance


# ==========================================================
# RECURSIVE BISECTION
# ==========================================================

def recursive_bisection(
    cov,
    sorted_items
):

    weights = pd.Series(
        1,
        index=sorted_items
    )

    clusters = [sorted_items]

    while len(clusters) > 0:

        clusters = [

            cluster[start:end]

            for cluster in clusters

            for start, end in (
                (0, len(cluster)//2),
                (len(cluster)//2, len(cluster))
            )

            if len(cluster) > 1
        ]

        for i in range(
            0,
            len(clusters),
            2
        ):

            cluster1 = clusters[i]

            cluster2 = clusters[i + 1]

            var1 = cluster_variance(
                cov,
                cluster1
            )

            var2 = cluster_variance(
                cov,
                cluster2
            )

            alpha = (
                1 -
                var1 /
                (var1 + var2)
            )

            weights[cluster1] *= alpha

            weights[cluster2] *= (
                1 - alpha
            )

    return weights


# ==========================================================
# HRP WEIGHTS
# ==========================================================

def hrp_weights(
    returns_df
):

    cov = returns_df.cov()

    corr = returns_df.corr()

    dist = correlation_distance(
        corr
    )

    link = linkage(
        squareform(dist),
        method="single"
    )

    sorted_ix = get_quasi_diag(
        link
    )

    sorted_names = corr.index[
        sorted_ix
    ]

    weights = recursive_bisection(
        cov,
        sorted_names
    )

    weights /= weights.sum()

    return weights


# ==========================================================
# HRP PORTFOLIO
# ==========================================================

def hrp_portfolio(
    returns_df
):

    weights = hrp_weights(
        returns_df
    )

    portfolio = (
        returns_df * weights
    ).sum(axis=1)

    return portfolio, weights