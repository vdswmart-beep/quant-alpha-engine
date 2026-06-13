def evaluate_alpha(
    metrics
):

    if metrics is None:
        return -999

    score = (
        metrics["sharpe"]
        * 0.7
        +
        metrics["return"]
        * 0.3
    )

    return float(score)