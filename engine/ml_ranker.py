import pandas as pd

from sklearn.ensemble import (
    RandomForestClassifier
)


class MLRanker:

    def __init__(self):

        self.model = RandomForestClassifier(

            n_estimators=500,

            max_depth=6,

            random_state=42,

            n_jobs=-1

        )

    def fit(self, X, y):

        self.model.fit(X, y)

    def predict_probability(self, X):

        return self.model.predict_proba(X)[:, 1]

    def feature_importance(self, cols):

        return pd.DataFrame(
            {
                "feature": cols,
                "importance":
                self.model.feature_importances_
            }
        ).sort_values(
            "importance",
            ascending=False
        )