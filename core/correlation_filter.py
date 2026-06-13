import numpy as np


def remove_correlated_alphas(
    returns_df,
    threshold=0.85
):

    corr = returns_df.corr()

    keep = []

    for col in corr.columns:

        if len(keep) == 0:
            keep.append(col)
            continue

        high_corr = False

        for existing in keep:

            if abs(
                corr.loc[col, existing]
            ) > threshold:

                high_corr = True

        if not high_corr:
            keep.append(col)

    return returns_df[keep]


# backward compatibility

def filter_correlated_strategies(
    returns_df,
    threshold=0.85
):

    return remove_correlated_alphas(
        returns_df,
        threshold
    )