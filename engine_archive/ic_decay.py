import pandas as pd


def ic_decay(
    signal,
    returns
):

    decay = []

    for horizon in [

        1,
        5,
        10,
        20,
        60

    ]:

        future = (

            returns
            .shift(-horizon)

        )

        ic = signal.corr(
            future
        )

        decay.append({

            "horizon":
            horizon,

            "ic":
            ic

        })

    return pd.DataFrame(
        decay
    )