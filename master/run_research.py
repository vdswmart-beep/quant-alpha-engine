import yfinance as yf
import pandas as pd

from engine.alpha_research_loop import (
    AlphaResearchLoop
)


def run_research():

    df = yf.download(
        "SPY",
        start="2015-01-01",
        auto_adjust=True
    )
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(level=1)

    research = AlphaResearchLoop(
        df=df,
        n_candidates=200,
        top_n=20
    )

    return research.run()


if __name__ == "__main__":

    run_research()