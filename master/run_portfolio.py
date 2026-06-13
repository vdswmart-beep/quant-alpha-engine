import yfinance as yf
import pandas as pd

from research.memory import load_json, ALPHA_LIBRARY
from engine.alpha_expression_engine import AlphaExpressionEngine
from core.portfolio import inverse_vol_portfolio


def run_portfolio():

    print("\nLoading market data...")

    df = yf.download(
        "SPY",
        start="2015-01-01",
        auto_adjust=True
    )
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(level=1)

    close = df["Close"]
    returns = close.pct_change()

    print("Loading alpha library...")

    alphas = load_json(ALPHA_LIBRARY)

    if len(alphas) == 0:
        print("No alphas found.")
        return None

    # Sort by robustness
    alphas = sorted(alphas, key=lambda x: x.get("rb_score", 0), reverse=True)

    top_n = min(10, len(alphas))
    selected = alphas[:top_n]

    print(f"Selected {len(selected)} alphas")

    engine = AlphaExpressionEngine()

    strategy_returns = {}

    for i, alpha in enumerate(selected):

        expr = alpha.get("expression")

        if expr is None:
            continue

        signal = engine.evaluate(expr, df)

        if signal is None:
            continue

        # ── FIX: normalize signal to zero-mean, unit-vol before applying ──
        sig_std = signal.std()
        if sig_std > 0:
            signal = (signal - signal.mean()) / sig_std
        signal = signal.clip(-3, 3) / 3  # scale to [-1, 1]
        # ──────────────────────────────────────────────────────────────────

        strat_ret = (signal.shift(1) * returns)

        strat_ret = strat_ret.replace([float("inf"), -float("inf")], 0).fillna(0)

        strategy_returns[f"alpha_{i}"] = strat_ret

    if len(strategy_returns) == 0:
        print("No valid strategies.")
        return None

    returns_df = pd.DataFrame(strategy_returns)

    # align clean
    returns_df = returns_df.dropna(how="all")

    print("\nBuilding portfolio...")

    portfolio_returns, weights = inverse_vol_portfolio(returns_df)

    portfolio_returns = portfolio_returns.replace([float("inf"), -float("inf")], 0).fillna(0)

    print("\nPortfolio weights:")
    print(weights)

    print("\nPortfolio performance:")
    mean = portfolio_returns.mean()
    vol = portfolio_returns.std()

    sharpe = 0 if vol == 0 else mean / vol

    print("Mean:", mean)
    print("Vol:", vol)
    print("Sharpe:", sharpe)

    return {
        "returns": portfolio_returns,
        "weights": weights,
        "strategies": returns_df
    }