import pandas as pd


def sensitivity_scan(
    test_function,
    parameters
):

    results = []

    for p in parameters:

        score = test_function(p)

        results.append(
            {
                "parameter": p,
                "score": score
            }
        )

    return pd.DataFrame(results)