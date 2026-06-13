import numpy as np

from sklearn.metrics import (
    accuracy_score
)


def walkforward_ml(
    model,
    X,
    y,
    train_size=500,
    test_size=60
):

    scores = []

    start = 0

    while True:

        train_end = (
            start
            + train_size
        )

        test_end = (
            train_end
            + test_size
        )

        if test_end > len(X):

            break

        X_train = X.iloc[
            start:train_end
        ]

        y_train = y.iloc[
            start:train_end
        ]

        X_test = X.iloc[
            train_end:test_end
        ]

        y_test = y.iloc[
            train_end:test_end
        ]

        model.fit(
            X_train,
            y_train
        )

        pred = (
            model
            .predict_probability(
                X_test
            )
            > 0.5
        )

        scores.append(

            accuracy_score(
                y_test,
                pred
            )

        )

        start += test_size

    return np.mean(scores)