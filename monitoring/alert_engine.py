def check_alerts(
    drawdown,
    sharpe
):

    alerts = []

    if drawdown < -0.15:

        alerts.append(
            "DRAWDOWN ALERT"
        )

    if sharpe < 0:

        alerts.append(
            "NEGATIVE SHARPE"
        )

    return alerts