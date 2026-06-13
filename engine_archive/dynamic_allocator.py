def dynamic_allocation(
    regime
):

    if regime == "Bull":

        return {
            "Trend": 0.40,
            "AdaptiveTrend": 0.30,
            "Breakout": 0.20,
            "MeanReversion": 0.10,
        }

    elif regime == "Bear":

        return {
            "Trend": 0.15,
            "AdaptiveTrend": 0.15,
            "Breakout": 0.20,
            "MeanReversion": 0.50,
        }

    elif regime == "Crash":

        return {
            "Trend": 0.05,
            "AdaptiveTrend": 0.05,
            "Breakout": 0.10,
            "MeanReversion": 0.30,
            "Cash": 0.50,
        }

    return {
        "Trend": 0.25,
        "AdaptiveTrend": 0.25,
        "Breakout": 0.25,
        "MeanReversion": 0.25,
    }