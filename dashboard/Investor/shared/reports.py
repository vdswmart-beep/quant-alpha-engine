import pandas as pd


def load_portfolio():

    df = pd.read_csv(
        "outputs/portfolio_equity.csv",
        index_col=0,
        parse_dates=True
    )

    df.columns = [
        c.lower()
        for c in df.columns
    ]

    for col in df.columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


def load_strategy_results():

    df = pd.read_csv(
        "outputs/strategy_results.csv"
    )

    numeric_cols = [
        "return",
        "sharpe",
        "sortino",
        "calmar",
        "hit_ratio",
        "drawdown",
        "stability",
        "score"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df