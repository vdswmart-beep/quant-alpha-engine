import pandas as pd


def build_ml_dataset(df):

    features = [

        c

        for c in df.columns

        if c not in [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ]

    X = df[features]

    y = (
        df["Close"]
        .pct_change()
        .shift(-5)
    )

    y = (y > 0).astype(int)

    dataset = pd.concat(
        [X, y.rename("target")],
        axis=1
    )

    dataset = dataset.dropna()

    return dataset