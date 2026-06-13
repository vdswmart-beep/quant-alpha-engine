from strategies.trend import trend_strategy
from strategies.mean_reversion import mean_reversion_strategy
from strategies.breakout import breakout_strategy


STRATEGIES = {
    "trend": trend_strategy,
    "mean_reversion": mean_reversion_strategy,
    "breakout": breakout_strategy
}
