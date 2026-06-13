import numpy as np


def bootstrap_sharpe(
    returns,
    n_bootstrap=1000
):

    sharpes = []

    returns = np.array(returns)

    for _ in range(n_bootstrap):

        sample = np.random.choice(
            returns,
            size=len(returns),
            replace=True
        )

        vol = sample.std()

        if vol == 0:
            continue

        sharpe = (
            sample.mean()
            / vol
        ) * np.sqrt(252)

        sharpes.append(sharpe)

    return {
        "mean":
            np.mean(sharpes),
        "p5":
            np.percentile(sharpes, 5),
        "p95":
            np.percentile(sharpes, 95)
    }