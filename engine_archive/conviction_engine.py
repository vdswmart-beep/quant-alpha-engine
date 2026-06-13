def conviction_score(
    sharpe,
    sortino,
    calmar,
    stability,
    hit_ratio,
):

    return (
        sharpe * 0.30
        + sortino * 0.20
        + calmar * 0.15
        + stability * 0.25
        + hit_ratio * 0.10
    )