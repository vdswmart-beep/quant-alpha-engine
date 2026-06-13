import pandas as pd
from datetime import datetime


class OrderManager:

    def __init__(self):

        self.orders = []

    def create_order(
        self,
        symbol,
        qty,
        side
    ):

        self.orders.append(

            {

                "timestamp":
                datetime.utcnow(),

                "symbol":
                symbol,

                "qty":
                qty,

                "side":
                side

            }

        )

    def export(self):

        return pd.DataFrame(
            self.orders
        )