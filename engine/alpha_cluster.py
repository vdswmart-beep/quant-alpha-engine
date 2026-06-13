import pandas as pd
import numpy as np

from sklearn.cluster import AgglomerativeClustering


def cluster_alphas(
    alpha_returns,
    n_clusters=10
):

    corr = (
        alpha_returns
        .corr()
        .fillna(0)
    )

    distance = (
        1 - corr.abs()
    )

    model = AgglomerativeClustering(
        n_clusters=min(
            n_clusters,
            len(corr)
        )
    )

    labels = model.fit_predict(
        distance
    )

    return pd.DataFrame(
        {
            "alpha": corr.index,
            "cluster": labels
        }
    )