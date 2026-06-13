from engine.book_builder import (
    build_alpha_books
)

from engine.meta_portfolio import (
    build_meta_portfolio
)


class PortfolioPipeline:

    def run(
        self,
        alpha_universe,
        clusters
    ):

        books = build_alpha_books(

            alpha_universe,

            clusters

        )

        portfolio_returns, weights = (

            build_meta_portfolio(
                books
            )

        )

        return {

            "books":
            books,

            "returns":
            portfolio_returns,

            "weights":
            weights
        }