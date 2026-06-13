from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

import matplotlib.pyplot as plt


def build_clusters(corr):

    distance = 1 - corr

    linkage_matrix = linkage(
        distance,
        method="ward"
    )

    return linkage_matrix


def plot_clusters(corr):

    distance = 1 - corr

    linkage_matrix = linkage(
        distance,
        method="ward"
    )

    plt.figure(figsize=(12, 8))

    dendrogram(
        linkage_matrix,
        labels=corr.columns
    )

    plt.tight_layout()

    plt.show()
