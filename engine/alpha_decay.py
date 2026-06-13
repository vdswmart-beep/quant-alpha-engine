def alpha_decay(
    recent_sharpe,
    long_sharpe
):

    return (
        recent_sharpe
        - long_sharpe
    )
