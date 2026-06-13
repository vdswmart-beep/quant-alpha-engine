import pandas as pd


def load_strategy_results():
    return pd.read_csv("outputs/strategy_results.csv")


def load_walkforward():
    return pd.read_csv("outputs/walkforward_results.csv")


def load_optimizer():
    return pd.read_csv("outputs/optimization_results.csv")


def load_correlation():
    return pd.read_csv(
        "outputs/correlation_matrix.csv",
        index_col=0
    )


def load_rankings():
    return pd.read_csv("outputs/rankings.csv")