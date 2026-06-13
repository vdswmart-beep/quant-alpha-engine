import pandas as pd


class PaperTrader:

    def __init__(self):

        self.positions = {}

    def send_order(
        self,
        symbol,
        quantity
    ):

        self.positions[
            symbol
        ] = quantity

        print(
            f"ORDER: {symbol} {quantity}"
        )