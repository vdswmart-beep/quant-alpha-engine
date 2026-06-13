import yfinance as yf
import pandas as pd

from engine.alpha_research_loop import (
    AlphaResearchLoop
)


class ResearchPipeline:

    def run(self):

        df = yf.download("SPY", start="2015-01-01", auto_adjust=True)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(level=1)
        close = df["Close"] 

        loop = AlphaResearchLoop()

        winners = loop.run(

            market_data=df,

            n_candidates=100,

            top_n=20

        )

        return winners