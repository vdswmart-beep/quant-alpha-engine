import pandas as pd


def build_features(df):

    df = df.copy()

    returns = df["Close"].pct_change()

    df["ret_5"] = returns.rolling(5).sum()

    df["ret_20"] = returns.rolling(20).sum()

    df["vol_20"] = returns.rolling(20).std()

    df["vol_60"] = returns.rolling(60).std()

    df["ma20"] = df["Close"].rolling(20).mean()

    df["ma50"] = df["Close"].rolling(50).mean()

    df["ma200"] = df["Close"].rolling(200).mean()

    return df